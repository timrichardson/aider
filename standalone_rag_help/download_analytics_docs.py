
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

# --- Configuration ---
START_URL = "https://www.zoho.com/analytics/help/overview.html"
# Base path to stay within (only crawl links starting with this)
BASE_PATH_PREFIX = "/analytics/help/"
# Base domain to stay within
BASE_DOMAIN = "www.zoho.com"
# Maximum crawl depth (0 = start page only, 1 = start page + links, etc.)
MAX_DEPTH = 3
# Output directory for markdown files and metadata map
OUTPUT_DIR_NAME = "training_data_zoho_analytics"
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


def main():
    print("Starting Zoho Analytics documentation download...")

    # Ensure the output directory exists within the script's package location
    script_dir = Path(__file__).parent
    output_dir = script_dir / OUTPUT_DIR_NAME
    output_dir.mkdir(exist_ok=True)
    print(f"Output directory: {output_dir}")

    queue = deque([(START_URL, 0)]) # Store (url, depth)
    visited = set()
    metadata = [] # List to store (relative_path_str, original_url) for CSV

    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0 (compatible; Python-Doc-Downloader/1.0)'})

    while queue:
        current_url, depth = queue.popleft()

        if current_url in visited or depth > MAX_DEPTH:
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

            # Use detected encoding or fallback to UTF-8
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
            # 1. Extract main content using Trafilatura
            # favour_recall=True might get more, but could include boilerplate
            extracted_html = trafilatura.extract(html_content,
                                                 include_comments=False,
                                                 include_tables=True) # Removed favour_recall argument

            if not extracted_html:
                print(f"  Trafilatura could not extract main content from {current_url}. Skipping save.")
                markdown_content = None
            else:
                # 2. Convert extracted HTML to Markdown
                # heading_style="ATX" uses # for headers
                markdown_content = markdownify(extracted_html, heading_style="ATX", bullets="-")

            # 3. Save Markdown and collect metadata (only if content exists)
            if markdown_content:
                local_path, csv_relative_path = url_to_local_path(current_url, BASE_PATH_PREFIX, output_dir)

                if local_path and csv_relative_path:
                    try:
                        local_path.parent.mkdir(parents=True, exist_ok=True)
                        with open(local_path, 'w', encoding='utf-8') as f:
                            f.write(markdown_content)
                        print(f"  Saved markdown to: {local_path.relative_to(script_dir)}")
                        metadata.append((csv_relative_path, current_url))
                    except OSError as e:
                        print(f"  Error saving file {local_path}: {e}")
                    except Exception as e:
                         print(f"  Unexpected error saving file {local_path}: {e}")
                else:
                     print(f"  Could not determine valid local path for {current_url}. Skipping save.")

        except Exception as e:
            print(f"  Error processing content for {current_url}: {e}")
            # Continue to find links even if processing fails

        # --- Find and enqueue valid links for next level ---
        if depth < MAX_DEPTH:
            try:
                soup = BeautifulSoup(html_content, 'html.parser')
                links_found = 0
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    # Construct absolute URL
                    absolute_url = urljoin(current_url, href)
                    # Clean URL (remove fragment)
                    parsed_absolute = urlparse(absolute_url)
                    cleaned_url = parsed_absolute._replace(fragment="").geturl()

                    if cleaned_url not in visited and should_crawl(cleaned_url, BASE_DOMAIN, BASE_PATH_PREFIX):
                        queue.append((cleaned_url, depth + 1))
                        links_found += 1
                # print(f"  Found {links_found} valid links to queue.") # Optional debug
            except Exception as e:
                 print(f"  Error parsing links on {current_url}: {e}")


    print(f"\nCrawl finished. Visited {len(visited)} pages.")

    # --- Write Metadata Map ---
    if metadata:
        csv_path = output_dir / "metadata_map.csv"
        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['relative_path', 'url']) # Header
                # Sort metadata by relative path for consistency
                metadata.sort(key=lambda x: x[0])
                writer.writerows(metadata)
            print(f"Metadata map saved to: {csv_path.relative_to(script_dir)}")
        except OSError as e:
            print(f"Error writing metadata map {csv_path}: {e}")
        except Exception as e:
             print(f"Unexpected error writing metadata map {csv_path}: {e}")
    else:
        print("No metadata collected, skipping metadata map generation.")

    print("Script completed.")

if __name__ == "__main__":
    main()
