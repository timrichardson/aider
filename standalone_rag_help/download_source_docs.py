
import os
import csv
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
from collections import deque
import trafilatura
from markdownify import markdownify
import re # Import re for validation

# --- Source Configurations ---
# List of sources to process. Add more dictionaries to this list.
SOURCES_CONFIG = [
    {
        "source_name": "zoho_analytics", # lowercase, no whitespace
        "source_type": "website",
        "details": {
            "start_url": "https://www.zoho.com/analytics/help/overview.html",
            "base_path_prefix": "/analytics/help/", # Path prefix to stay within
            "base_domain": "www.zoho.com",         # Domain to stay within
            "max_depth": 3,                        # Max crawl depth
        }
    },
    # Example for adding another source (e.g., Aider docs if needed)
    # {
    #     "source_name": "aider_docs",
    #     "source_type": "website",
    #     "details": {
    #         "start_url": "https://aider.chat/docs/",
    #         "base_path_prefix": "/docs/",
    #         "base_domain": "aider.chat",
    #         "max_depth": 2,
    #     }
    # },
    # {
    #     "source_name": "specific_pages",
    #     "source_type": "list_of_urls",
    #     "details": {
    #         "urls": [
    #             "https://example.com/important-page-1",
    #             "https://another.net/docs/feature-x.html",
    #         ]
    #     }
    # },
]

# --- General Configuration ---
# Delay between requests (in seconds) to be polite
REQUEST_DELAY = 0.5
# --- End Configuration ---

def is_valid_url(url):
    """Check if the URL scheme is http or https."""
    parsed = urlparse(url)
    return parsed.scheme in ["http", "https"]

def should_crawl(url, base_domain, base_path_prefix):
    """Check if the URL should be crawled based on domain and path prefix."""
    parsed = urlparse(url)
    # Ensure it's the correct domain
    if parsed.netloc.lower() != base_domain.lower():
        return False
    # Ensure the path starts with the desired prefix
    if not parsed.path.startswith(base_path_prefix):
        return False
    # Avoid crawling non-html files if possible (basic check)
    if '.' in parsed.path.split('/')[-1] and not parsed.path.lower().endswith(('.html', '.htm')):
         # Allow URLs with extensions only if they are html/htm
         return False
    # Allow URLs with no extension or ending in / or .html/.htm
    return True


def url_to_local_path(url, base_path_prefix, output_dir):
    """Converts a valid crawled URL to a local markdown file path."""
    parsed = urlparse(url)
    path = parsed.path

    # Remove the base prefix to get the relative path
    if path.startswith(base_path_prefix):
        relative_path = path[len(base_path_prefix):]
    else:
        # Should not happen if should_crawl is used correctly
        print(f"Warning: URL '{url}' does not start with expected prefix '{base_path_prefix}'")
        return None, None

    # Clean the relative path
    relative_path = relative_path.strip('/')
    # If the original path ended with .html, remove it for directory structure
    if relative_path.lower().endswith(".html"):
        relative_path = relative_path[:-5]
    elif relative_path.lower().endswith(".htm"):
         relative_path = relative_path[:-4]

    # If the path is now empty, it was the index of the base prefix
    if not relative_path:
        relative_path = "index"

    # Ensure forward slashes for internal consistency
    relative_path = relative_path.replace("\\", "/")

    # Create the full local path
    local_path = output_dir / Path(relative_path + ".md")

    # Return both the full path and the relative path string for the CSV
    # Ensure relative path for CSV also uses forward slashes
    csv_relative_path = relative_path + ".md"

    return local_path, csv_relative_path

def validate_source_name(name):
    """Check if source_name is lowercase and has no whitespace."""
    if not name:
        return False, "Source name cannot be empty."
    if name != name.lower():
        return False, f"Source name '{name}' must be lowercase."
    if re.search(r'\s', name):
        return False, f"Source name '{name}' cannot contain whitespace."
    return True, ""

def url_to_filename(url):
    """Creates a safe filename from a URL, preserving some structure."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path: # Handle root URLs
        path = parsed.netloc + "_index"
    else:
        # Combine domain and path for uniqueness if needed, or just use path
        path = parsed.netloc + "_" + path

    # Remove common extensions
    path = re.sub(r'\.(html|htm|php|asp|aspx)$', '', path, flags=re.IGNORECASE)

    # Replace invalid filename characters with underscores
    safe_filename = re.sub(r'[<>:"/\\|?*]+', '_', path)
    # Replace multiple consecutive underscores with a single one
    safe_filename = re.sub(r'_+', '_', safe_filename)
    # Limit length
    max_len = 100
    if len(safe_filename) > max_len:
        # Keep the end part, which might be more specific
        safe_filename = safe_filename[-max_len:]

    return safe_filename + ".md"


def process_website_source(config, script_dir):
    """Handles crawling and processing for a 'website' type source."""
    source_name = config["source_name"]
    details = config["details"]
    start_url = details["start_url"]
    base_path_prefix = details["base_path_prefix"]
    base_domain = details["base_domain"]
    max_depth = details["max_depth"]

    output_dir_name = f"training_data_{source_name}"
    output_dir = script_dir / output_dir_name
    output_dir.mkdir(exist_ok=True)
    print(f"\n--- Processing Source: {source_name} ---")
    print(f"Output directory: {output_dir}")
    print(f"Start URL: {start_url}")

    queue = deque([(start_url, 0)]) # Store (url, depth)
    visited = set()
    metadata = [] # List to store (relative_path_str, original_url) for CSV
    processed_local_paths = set() # Keep track of files generated in this run

    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; Python-Doc-Downloader/1.0)'})

    while queue:
        current_url, depth = queue.popleft()

        if current_url in visited or depth > max_depth:
            continue

        if not is_valid_url(current_url):
            print(f"Skipping invalid URL scheme: {current_url}")
            continue

        visited.add(current_url)
        print(f"Processing (Depth {depth}): {current_url}")

        try:
            time.sleep(REQUEST_DELAY) # Be polite
            response = session.get(current_url, timeout=15)
            response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
            response.encoding = response.apparent_encoding or 'utf-8'
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"  Error fetching {current_url}: {e}")
            continue
        except Exception as e:
             print(f"  Unexpected error fetching {current_url}: {e}")
             continue

        # --- Process the current page ---
        try:
            extracted_html = trafilatura.extract(html_content, include_comments=False, include_tables=True)
            if not extracted_html:
                print(f"  Trafilatura could not extract main content from {current_url}. Skipping save.")
                markdown_content = None
            else:
                markdown_content = markdownify(extracted_html, heading_style="ATX", bullets="-")

            if markdown_content:
                local_path, csv_relative_path = url_to_local_path(current_url, base_path_prefix, output_dir)
                if local_path and csv_relative_path:
                    try:
                        local_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(local_path, 'w', encoding='utf-8') as f:
                            f.write(markdown_content)
                        # Use relative_to script_dir for consistent logging path
                        log_path = local_path.relative_to(script_dir) if local_path.is_relative_to(script_dir) else local_path
                        print(f"  Saved markdown to: {log_path}")
                        metadata.append((csv_relative_path, current_url))
                        processed_local_paths.add(local_path) # Track saved path
                    except OSError as e:
                        print(f"  Error saving file {local_path}: {e}")
                    except Exception as e:
                         print(f"  Unexpected error saving file {local_path}: {e}")
                else:
                     print(f"  Could not determine valid local path for {current_url}. Skipping save.")
        except Exception as e:
            print(f"  Error processing content for {current_url}: {e}")

        # --- Find and enqueue valid links for next level ---
        if depth < max_depth:
            try:
                soup = BeautifulSoup(html_content, 'html.parser')
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    absolute_url = urljoin(current_url, href)
                    parsed_absolute = urlparse(absolute_url)
                    cleaned_url = parsed_absolute._replace(fragment="").geturl()
                    if cleaned_url not in visited and should_crawl(cleaned_url, base_domain, base_path_prefix):
                        queue.append((cleaned_url, depth + 1))
            except Exception as e:
                 print(f"  Error parsing links on {current_url}: {e}")

    print(f"\nCrawl finished for {source_name}. Visited {len(visited)} pages.")

    # --- Write Metadata Map ---
    if metadata:
        csv_path = output_dir / "metadata_map.csv"
        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['relative_path', 'url']) # Header
                metadata.sort(key=lambda x: x[0])
                writer.writerows(metadata)
            # Use relative_to script_dir for consistent logging path
            log_csv_path = csv_path.relative_to(script_dir) if csv_path.is_relative_to(script_dir) else csv_path
            print(f"Metadata map saved to: {log_csv_path}")
        except OSError as e:
            print(f"Error writing metadata map {csv_path}: {e}")
        except Exception as e:
             print(f"Unexpected error writing metadata map {csv_path}: {e}")
    else:
        print(f"No metadata collected for {source_name}, skipping metadata map generation.")

    # --- Cleanup Stale Files ---
    print(f"\nCleaning up stale files in {output_dir.relative_to(script_dir)}...")
    stale_count = 0
    try:
        for existing_file in output_dir.rglob("*.md"):
            if existing_file.is_file():
                # Ensure comparison is between Path objects
                if existing_file not in processed_local_paths:
                    try:
                        log_stale_path = existing_file.relative_to(script_dir) if existing_file.is_relative_to(script_dir) else existing_file
                        print(f"  Deleting stale file: {log_stale_path}")
                        existing_file.unlink() # Delete the file
                        stale_count += 1
                    except OSError as e:
                        print(f"  Error deleting stale file {existing_file}: {e}")
                    except Exception as e:
                        print(f"  Unexpected error deleting stale file {existing_file}: {e}")
    except Exception as e:
         print(f"Error during stale file cleanup scan for {source_name}: {e}")

    if stale_count > 0:
        print(f"Deleted {stale_count} stale markdown file(s).")
    else:
        print("No stale markdown files found to delete.")
    # --- End Cleanup ---


def process_list_of_urls_source(config, script_dir):
    """Handles fetching and processing for a 'list_of_urls' type source."""
    source_name = config["source_name"]
    details = config["details"]
    urls_to_process = details["urls"]

    output_dir_name = f"training_data_{source_name}"
    output_dir = script_dir / output_dir_name
    output_dir.mkdir(exist_ok=True)
    print(f"\n--- Processing Source: {source_name} (List of URLs) ---")
    print(f"Output directory: {output_dir}")
    print(f"Processing {len(urls_to_process)} URL(s).")

    metadata = [] # List to store (relative_path_str, original_url) for CSV
    processed_local_paths = set() # Keep track of files generated in this run

    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; Python-Doc-Downloader/1.0)'})

    for i, current_url in enumerate(urls_to_process):
        print(f"Processing URL {i+1}/{len(urls_to_process)}: {current_url}")

        if not is_valid_url(current_url):
            print(f"  Skipping invalid URL scheme: {current_url}")
            continue

        try:
            time.sleep(REQUEST_DELAY) # Be polite
            response = session.get(current_url, timeout=15)
            response.raise_for_status()
            response.encoding = response.apparent_encoding or 'utf-8'
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"  Error fetching {current_url}: {e}")
            continue
        except Exception as e:
             print(f"  Unexpected error fetching {current_url}: {e}")
             continue

        # --- Process the current page ---
        try:
            extracted_html = trafilatura.extract(html_content, include_comments=False, include_tables=True)
            if not extracted_html:
                print(f"  Trafilatura could not extract main content from {current_url}. Skipping save.")
                continue # Skip if no content

            markdown_content = markdownify(extracted_html, heading_style="ATX", bullets="-")

            # Generate filename based on URL
            filename = url_to_filename(current_url)
            local_path = output_dir / filename
            csv_relative_path = filename # For this type, filename is the relative path

            try:
                local_path.parent.mkdir(parents=True, exist_ok=True) # Should just be output_dir
                with open(local_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)
                log_path = local_path.relative_to(script_dir) if local_path.is_relative_to(script_dir) else local_path
                print(f"  Saved markdown to: {log_path}")
                metadata.append((csv_relative_path, current_url))
                processed_local_paths.add(local_path) # Track saved path
            except OSError as e:
                print(f"  Error saving file {local_path}: {e}")
            except Exception as e:
                 print(f"  Unexpected error saving file {local_path}: {e}")

        except Exception as e:
            print(f"  Error processing content for {current_url}: {e}")

    print(f"\nFinished processing URLs for {source_name}.")

    # --- Write Metadata Map ---
    if metadata:
        csv_path = output_dir / "metadata_map.csv"
        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['relative_path', 'url']) # Header
                metadata.sort(key=lambda x: x[0]) # Sort by filename
                writer.writerows(metadata)
            log_csv_path = csv_path.relative_to(script_dir) if csv_path.is_relative_to(script_dir) else csv_path
            print(f"Metadata map saved to: {log_csv_path}")
        except OSError as e:
            print(f"Error writing metadata map {csv_path}: {e}")
        except Exception as e:
             print(f"Unexpected error writing metadata map {csv_path}: {e}")
    else:
        print(f"No metadata collected for {source_name}, skipping metadata map generation.")

    # --- Cleanup Stale Files ---
    # Cleanup logic remains the same, comparing existing *.md files against processed_local_paths
    print(f"\nCleaning up stale files in {output_dir.relative_to(script_dir)}...")
    stale_count = 0
    try:
        for existing_file in output_dir.rglob("*.md"):
            if existing_file.is_file():
                if existing_file not in processed_local_paths:
                    try:
                        log_stale_path = existing_file.relative_to(script_dir) if existing_file.is_relative_to(script_dir) else existing_file
                        print(f"  Deleting stale file: {log_stale_path}")
                        existing_file.unlink()
                        stale_count += 1
                    except OSError as e:
                        print(f"  Error deleting stale file {existing_file}: {e}")
                    except Exception as e:
                        print(f"  Unexpected error deleting stale file {existing_file}: {e}")
    except Exception as e:
         print(f"Error during stale file cleanup scan for {source_name}: {e}")

    if stale_count > 0:
        print(f"Deleted {stale_count} stale markdown file(s).")
    else:
        print("No stale markdown files found to delete.")
    # --- End Cleanup ---


def main():
    print("Starting documentation download script...")
    script_dir = Path(__file__).parent

    processed_count = 0
    for config in SOURCES_CONFIG:
        source_name = config.get("source_name")
        source_type = config.get("source_type")
        details = config.get("details")

        is_valid, error_msg = validate_source_name(source_name)
        if not is_valid:
            print(f"Skipping invalid source configuration: {error_msg}")
            continue

        if not source_type or not details:
             print(f"Skipping incomplete configuration for source: {source_name}")
             continue

        if source_type == "website":
            # Check required keys for website type
            required_keys = ["start_url", "base_path_prefix", "base_domain", "max_depth"]
            if not all(key in details for key in required_keys):
                 print(f"Skipping incomplete 'website' configuration for source: {source_name}. Missing keys.")
                 continue
            try:
                process_website_source(config, script_dir)
                processed_count += 1
            except Exception as e:
                 print(f"!!! Unexpected error processing source '{source_name}': {e}")
                 # Optionally add traceback here for debugging
                 # import traceback
                 # traceback.print_exc()
        elif source_type == "list_of_urls":
             # Check required keys for list_of_urls type
             if "urls" not in details or not isinstance(details["urls"], list):
                  print(f"Skipping incomplete 'list_of_urls' configuration for source: {source_name}. 'urls' key missing or not a list.")
                  continue
             try:
                 process_list_of_urls_source(config, script_dir)
                 processed_count += 1
             except Exception as e:
                  print(f"!!! Unexpected error processing source '{source_name}': {e}")
                  # import traceback
                  # traceback.print_exc()
        else:
            print(f"Skipping source '{source_name}': Unsupported source_type '{source_type}'")

    print(f"\nScript completed. Processed {processed_count} source(s).")

if __name__ == "__main__":
    main()
