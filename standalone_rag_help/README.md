# Standalone RAG Help

This tool provides a Retrieval-Augmented Generation (RAG) interface to query documentation, specifically designed initially for Aider's documentation.

## Installation

```bash
pip install .
```

## Adding Content to the RAG Database

This RAG system learns from text-based documents stored in one or more **training data directories**. Here's how to prepare and add your own content:

**1. Training Data Directories:**
*   The system automatically scans for directories named `training_data_*` directly inside the `standalone_rag_help` package directory (e.g., `standalone_rag_help/training_data_aider/`, `standalone_rag_help/training_data_zoho/`).
*   You can create multiple such directories to organize content from different sources. The original Aider docs should be placed in `standalone_rag_help/training_data_aider/`.

**2. Content Format:**
*   Inside each `training_data_*` directory, the primary format for content is **Markdown (`.md`)**. Ensure your files have the `.md` extension.
*   The content should be clean, well-structured text. Standard Markdown syntax (headings, lists, code blocks, paragraphs) is recommended for best parsing.

**3. Preparing Content:**
*   **Existing Markdown:** If you already have documentation in Markdown format, place the `.md` files into the relevant `standalone_rag_help/training_data_*/` directory (or subdirectories within it).
*   **Converting Websites:**
    *   **Manual:** For smaller amounts of content, you can manually copy text from web pages and paste it into new `.md` files within the appropriate `training_data_*` directory. Format the text using Markdown syntax.
    *   **Automated Tools:** For larger websites, you might use tools to help convert HTML to Markdown. Options include:
        *   **Recommended for Cleaning:** Libraries like **`trafilatura`** (Python library & CLI tool) are specifically designed to extract the main text content from a webpage, effectively removing boilerplate like navigation, ads, and footers *before* conversion. This often leads to much cleaner results.
            *   *Example CLI:* `pip install trafilatura` then `trafilatura -u YOUR_URL --markdown > output.md`
            *   *Example Python:* Use `trafilatura.fetch_url` and `trafilatura.extract` to get cleaned HTML, then convert that HTML using a library like `markdownify`.
        *   Browser extensions (e.g., MarkDownload) that often use cleaning libraries internally.
        *   General command-line tools like `pandoc` (`pandoc -f html -t markdown input.html -o output.md`), though these may require more manual cleanup of the output Markdown unless the source HTML is very clean.
        *   Other web scraping scripts combined with HTML-to-Markdown libraries (like `markdownify` or `html2text`).
    *   **Important:** Even with cleaning tools like `trafilatura`, automated conversion often requires some manual review and cleanup. Check the generated Markdown for formatting errors and ensure the core content is accurate before adding it to the training data. The cleaner the Markdown, the better the RAG results.

**4. Organizing Content:**
*   Place your `.md` files inside the relevant `standalone_rag_help/training_data_*/` directory.
*   You can create subdirectories within each `training_data_*` directory to organize your files (e.g., `training_data_zoho/guides/`, `training_data_aider/api_reference/`). The structure helps with organization but doesn't fundamentally change how the RAG system retrieves information (it searches across all indexed text).

**5. Handling Images:**
*   **Direct Indexing:** This RAG system primarily indexes and retrieves **text**. It does **not** directly analyze or understand the content of image files (like PNGs, JPGs).
*   **Descriptive Text:** If images are important, describe them in the Markdown text surrounding them. For example, instead of just having `![Diagram](diagram.png)`, add text like: "The following diagram illustrates the system architecture: ![Diagram](diagram.png) It shows the user interface connecting to the API gateway..." The descriptive text *will* be indexed.
*   **Storage:** You can store image files alongside your Markdown files (e.g., in an `assets` subdirectory within a `training_data_*` directory) for reference, but they won't be directly used by the RAG retrieval process. Ensure any such asset directories are *not* excluded by patterns in `config_patterns.py` if you want associated Markdown files referencing them to be included. (Note: The default `config_patterns.py` excludes `assets/**`, which applies relative to the training directory).

**6. URL Mapping (Optional but Recommended):**
*   Each `training_data_*` directory can optionally contain its own `metadata_map.csv` file to associate its documents with specific URLs. This URL is included in the metadata attached to the indexed document chunks.
*   **Create this file:** Place `metadata_map.csv` inside *each* relevant `standalone_rag_help/training_data_*/` directory alongside its `.md` files. Make sure these CSVs are included if you package/distribute the tool.
*   **Format:** The CSV must have exactly two columns with a header row: `relative_path` and `url`.
    ```csv
    relative_path,url
    docs/usage.md,https://example.com/usage-guide
    features/feature1.md,https://another-site.com/feature1-details
    index.md,https://example.com/home
    subdir/another_doc.md,https://example.com/another
    ```
*   **`relative_path`:** Use forward slashes (`/`) for the path relative to *its specific* `training_data_*` directory (e.g., `docs/usage.md` within `training_data_aider/metadata_map.csv`, not `/docs/usage.md` or `training_data_aider/docs/usage.md`).
*   **`url`:** Provide the full, absolute URL you want associated with the document.
*   **Behavior:** During indexing, the system looks for a `metadata_map.csv` in each `training_data_*` directory. If a document's relative path (within its directory) is found in its corresponding CSV, the URL is added to its metadata. Otherwise, the URL metadata will be empty. The indexing process will print info/warnings about loading these CSVs.

**7. Excluding Files:**
*   You can prevent specific files or directories from being indexed entirely by adding glob patterns to the `exclude_website_pats` list in `standalone_rag_help/config_patterns.py`. These patterns are applied relative to the root of each `training_data_*` directory (e.g., `examples/**` will exclude `training_data_aider/examples/` and `training_data_zoho/examples/`). Files/directories starting with `_` are also excluded by default patterns in this file.

**8. Rebuilding the Index:**
*   After adding or modifying files in *any* `training_data_*` directory, or changing `metadata_map.csv` files, the RAG index needs to be updated to include all sources correctly.
*   The tool automatically tries to build the index if it doesn't exist when you run `rag-help`.
*   To **force** a rebuild reflecting your new content, **delete the cache directory**: `~/.standalone_rag_cache/index.standalone_v1/`. The tool will then create a fresh index the next time it runs.

## Usage

```bash
rag-help "How do I use aider with git?"
```

## Managing Dependencies (for Developers)

This package manages its Python dependencies using `uv` and input/output requirement files:

*   **`standalone_rag_help/requirements.in`**: This file lists the *direct* dependencies of the standalone RAG tool. Add or remove packages here.
*   **`standalone_rag_help/requirements.txt`**: This file is *generated* by `uv pip compile`. It contains the full list of pinned dependencies, including transitive ones, ensuring reproducible installations. **Do not edit this file directly.**
*   **`requirements/common-constraints.txt`**: Located in the parent project directory, this file provides version constraints that are respected during compilation to ensure compatibility across the larger project.

To update dependencies after modifying `standalone_rag_help/requirements.in`, run the following command from the **project root directory** (the directory containing the main `aider` project and the `standalone_rag_help` subdirectory):

```bash
uv pip compile --no-strip-extras --constraint=requirements/common-constraints.txt --output-file=standalone_rag_help/requirements.txt standalone_rag_help/requirements.in
```

This command will:
1. Read the direct dependencies from `standalone_rag_help/requirements.in`.
2. Resolve all necessary transitive dependencies.
3. Apply version constraints from `requirements/common-constraints.txt`.
4. Write the complete, pinned list of packages to `standalone_rag_help/requirements.txt`.

Commit both the updated `requirements.in` and the regenerated `requirements.txt` file to version control.
