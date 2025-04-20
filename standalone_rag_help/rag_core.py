#!/usr/bin/env python

import json
import os
import csv # Add csv import
import shutil
import os # Ensure os is imported
import warnings
import sys
import subprocess
from pathlib import Path

try:
    import importlib.resources as importlib_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources

from .config_patterns import exclude_website_pats # Use local config

# LlamaIndex imports moved here
from llama_index.core import (
    Document,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
    Settings,
)
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# Ensure StorageContext and load_index_from_storage are imported
from llama_index.core import StorageContext, load_index_from_storage

# Import prompts to use the formatter
# fname_to_url is removed from prompts later
from .prompts import HelpPrompts


# Use a fixed version/name for the cache to avoid Aider version dependency
STANDALONE_RAG_VERSION = "standalone_v1"

warnings.simplefilter("ignore", category=FutureWarning)


def _check_import(package_name):
    """Checks if a package is installed."""
    import importlib
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def install_dependencies_if_needed():
    """
    Checks for core dependencies and prompts for installation if missing.
    Returns True if dependencies are met or installed, False otherwise.
    """
    required = {
        "llama_index.core": "llama-index-core",
        "llama_index.embeddings.huggingface": "llama-index-embeddings-huggingface",
        "torch": "torch",
        "sentence_transformers": "sentence-transformers",
    }
    missing = []
    for import_path, package_name in required.items():
        # Check submodule import paths correctly
        module_to_check = import_path.split('.')[0]
        if not _check_import(module_to_check):
             missing.append(package_name)

    if not missing:
        return True

    print("The RAG help feature requires some extra dependencies:")
    print(", ".join(missing))
    print("\nAttempting to install them now using pip.")
    print("If this fails, please install them manually:")
    install_cmd_base = [sys.executable, "-m", "pip", "install"]
    # Special handling for torch if needed, e.g., extra index URL
    # For simplicity, we'll try a direct install first.
    # Users might need to install torch manually following PyTorch official instructions
    # if the simple pip install doesn't work or they need a specific version (CPU/GPU).
    print(f"  pip install {' '.join(missing)}")

    try:
        # Install all missing packages at once
        subprocess.check_call(install_cmd_base + missing)
        print("Dependencies installed successfully.")
        # Re-verify after installation attempt
        import importlib
        for import_path, _ in required.items():
             module_to_check = import_path.split('.')[0]
             importlib.reload(importlib.import_module('importlib')) # Ensure import path is fresh
             if not _check_import(module_to_check):
                 print(f"Failed to import {module_to_check} even after installation attempt.", file=sys.stderr)
                 return False # Failed verification
        return True # Verified successfully
    except subprocess.CalledProcessError as e:
        print(f"\nError installing dependencies: {e}", file=sys.stderr)
        print("Please install the missing packages manually.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"\nAn unexpected error occurred during dependency installation: {e}", file=sys.stderr)
        return False


def get_package_files(package_name="standalone_rag_help"):
    """
    Yields tuples of (training_dir_path, file_path) for all markdown files
    within all 'training_data_*' directories in the package.
    """
    all_files_found = False
    try:
        package_root = importlib_resources.files(package_name)
        for item in package_root.iterdir():
            # Check if item is a directory and its name starts with "training_data_"
            # Use .name attribute for string comparison
            if item.is_dir() and item.name.startswith("training_data_"):
                training_dir_path = item
                print(f"Scanning training data directory: {training_dir_path.name}")
                found_in_dir = False
                for file_path in training_dir_path.rglob("*.md"):
                    if file_path.is_file():
                        yield (training_dir_path, file_path)
                        found_in_dir = True
                        all_files_found = True
                if not found_in_dir:
                     print(f"  No markdown files found in {training_dir_path.name}")

        if not all_files_found:
             print(f"Warning: No markdown files found in any 'training_data_*' directories within '{package_name}'.", file=sys.stderr)

    except Exception as e:
        print(f"Error accessing package data directories: {e}", file=sys.stderr)


# <<< REMOVED fname_to_url FUNCTION DEFINITION >>>

def get_index(force_rebuild=False):
    """
    Loads the index from cache or builds it if missing, corrupted, or force_rebuild is True.

    Args:
        force_rebuild (bool): If True, deletes any existing index and rebuilds it.

    Returns:
        VectorStoreIndex: The loaded or built index, or raises an error.
    """
    # Configure embedding model globally for LlamaIndex
    # Ensure TOKENIZERS_PARALLELISM is set appropriately
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    try:
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    except Exception as e:
        print(f"Error initializing embedding model: {e}", file=sys.stderr)
        print("Please ensure sentence-transformers, torch, and transformers are installed.", file=sys.stderr)
        raise # Re-raise the exception to halt execution

    # Use a dedicated cache directory for the standalone tool
    cache_base_dir = Path.home() / ".standalone_rag_cache"
    dname = cache_base_dir / ("index." + STANDALONE_RAG_VERSION)

    # --- Handle force_rebuild ---
    if force_rebuild and dname.exists():
        print(f"Force rebuild requested. Removing existing index at {dname}")
        try:
            shutil.rmtree(dname)
        except OSError as e:
            print(f"Error removing existing index for rebuild: {e}", file=sys.stderr)
            # Decide whether to raise or just warn and continue build attempt
            # Let's warn and continue for now.

    index = None
    # --- Attempt to load only if not forcing rebuild ---
    if not force_rebuild and dname.exists():
        try:
            storage_context = StorageContext.from_defaults(
                persist_dir=str(dname), # Ensure path is string
            )
            index = load_index_from_storage(storage_context)
            print(f"Loaded existing index from {dname}")
        except (OSError, json.JSONDecodeError, FileNotFoundError, TypeError, EOFError) as e: # Added more exceptions
            print(f"Could not load index from {dname}, will rebuild. Error: {e}")
            if dname.exists():
                try:
                    shutil.rmtree(dname)
                    print(f"Removed corrupted index directory {dname}")
                except OSError as rm_e:
                    print(f"Error removing corrupted index directory {dname}: {rm_e}", file=sys.stderr)
        except Exception as e:
            # Catch other potential LlamaIndex loading errors
            print(f"An unexpected error occurred loading the index: {e}", file=sys.stderr)
            if dname.exists():
                 try:
                     shutil.rmtree(dname)
                     print(f"Removed potentially problematic index directory {dname}")
                 except OSError as rm_e:
                     print(f"Error removing index directory {dname}: {rm_e}", file=sys.stderr)

    # --- Build index if needed (no index loaded or force_rebuild=True) ---
    if index is None:
        # This block executes if:
        # 1. force_rebuild was True (and existing index was removed)
        # 2. force_rebuild was False, but dname didn't exist
        # 3. force_rebuild was False, dname existed, but loading failed (and dname was removed)
        print("Building new RAG index...")
        parser = MarkdownNodeParser()

        # --- Load URL Mappings from all CSVs ---
        url_map = {} # Key: absolute file path string (posix), Value: url
        all_training_dirs = set() # Keep track of dirs found
        try:
            package_root = importlib_resources.files("standalone_rag_help")
            for item in package_root.iterdir():
                 # Check if item is a directory and its name starts with "training_data_"
                 if item.is_dir() and item.name.startswith("training_data_"):
                     training_dir_path = item
                     all_training_dirs.add(training_dir_path) # Keep track of dirs
                     csv_path_trav = training_dir_path / "metadata_map.csv" # This is a Traversable

                     # Convert Traversable to Path before filesystem checks
                     try:
                         csv_path = Path(str(csv_path_trav))
                     except Exception as path_conv_e:
                         print(f"Error converting CSV path {csv_path_trav} to standard Path: {path_conv_e}", file=sys.stderr)
                         continue # Skip this directory's CSV

                     if csv_path.is_file():
                         # Use relative_to for cleaner logging if possible
                         try:
                             # Use the Path object for relative_to
                             log_csv_path = csv_path.relative_to(Path(str(package_root)))
                         except ValueError:
                             log_csv_path = csv_path # Fallback if not relative
                         except Exception as e:
                             pass # Ignore errors getting relative path for logging
                         print(f"Loading URL map: {log_csv_path}")
                         try:
                             # Use the Path object for open()
                             with csv_path.open('r', newline='', encoding='utf-8') as csvfile:
                                 reader = csv.reader(csvfile)
                                 header = next(reader) # Read header row
                                 if header != ['relative_path', 'url']:
                                      print(f"Warning: Unexpected header in {log_csv_path}: {header}", file=sys.stderr)
                                      # Attempt to proceed assuming correct columns anyway, or skip file? Let's proceed.
                                 for i, row in enumerate(reader):
                                     if len(row) == 2:
                                         relative_path, url = row
                                         # Normalize relative path key from CSV
                                         rel_path_key = relative_path.strip().replace("\\", "/")
                                         # Construct absolute path for the map key:
                                         # Use the already converted Path object 'training_dir_path'
                                         abs_file_path_obj = Path(str(training_dir_path)) / rel_path_key
                                         resolved_path = abs_file_path_obj.resolve()
                                         # Store with POSIX path separator for consistency
                                         url_map[resolved_path.as_posix()] = url.strip()
                                     else:
                                          print(f"Warning: Skipping malformed row {i+2} in {log_csv_path}: {row}", file=sys.stderr)
                         except StopIteration:
                             print(f"Warning: {log_csv_path} is empty or has only a header.", file=sys.stderr)
                         except csv.Error as csv_e:
                             print(f"Error reading CSV data from {log_csv_path}: {csv_e}", file=sys.stderr)
                         except Exception as e:
                             print(f"Error processing {log_csv_path}: {e}", file=sys.stderr)
                     else:
                         print(f"Info: No metadata_map.csv found in {training_dir_path.name}.")
        except Exception as e:
            print(f"Error discovering training directories or loading CSVs: {e}", file=sys.stderr)
        # --- End URL Mapping Loading ---

        nodes = []
        # get_package_files now yields (training_dir_path, file_path) tuples
        packaged_files_with_context = list(get_package_files())
        if not packaged_files_with_context:
             print("Error: No markdown documentation files found in any 'training_data_*' directories.", file=sys.stderr)
             print("Please ensure at least one 'training_data_*' directory exists and contains markdown files.", file=sys.stderr)
             # Decide how to handle this - raise error or return None?
             # Raising an error might be better to indicate setup issue.
             raise FileNotFoundError("No documentation files found to build index.")


        for training_dir_path_trav, fname_path_trav in packaged_files_with_context:
            # --- Convert Traversable paths to standard Path objects ---
            try:
                # Convert using str() to get the path string representation
                training_dir_path = Path(str(training_dir_path_trav))
                fname_path = Path(str(fname_path_trav))
            except Exception as path_conv_e:
                 print(f"Error converting package path to standard Path: {path_conv_e}", file=sys.stderr)
                 print(f"  Skipping file: {fname_path_trav}", file=sys.stderr)
                 continue
            # --- End Conversion ---

            # Calculate path relative to its specific training dir for exclusion checks
            relative_path_for_exclude = None
            try:
                # Use relative_to with standard Path objects
                relative_path_for_exclude = fname_path.relative_to(training_dir_path)
            except ValueError:
                 # This can happen if fname_path is somehow not under training_dir_path
                 # (Should be less likely now with explicit Path conversion)
                 print(f"Warning: File {fname_path} seems outside its reported training dir {training_dir_path}. Skipping exclusion check.", file=sys.stderr)

            # Perform exclusion check only if relative path could be determined
            # Use standard Path.match method
            if relative_path_for_exclude and any(relative_path_for_exclude.match(pat) for pat in exclude_website_pats):
                # print(f"Excluding {relative_path_for_exclude} based on patterns.") # Optional debug print
                continue

            try:
                # --- Get URL from mapping using absolute path ---
                # Use standard Path.resolve() and .as_posix()
                abs_path_key = fname_path.resolve().as_posix()
                doc_url = url_map.get(abs_path_key, "") # Default to empty URL if not found
                # --- End Get URL ---

                # Determine the display filename (relative path if possible, else just name)
                # Use standard Path.name attribute
                display_filename = str(relative_path_for_exclude) if relative_path_for_exclude else fname_path.name
                # Ensure display_filename uses forward slashes for consistency
                display_filename = display_filename.replace("\\", "/")

                doc = Document(
                    # Use standard Path.read_text()
                    text=fname_path.read_text(encoding="utf-8"),
                    metadata=dict(
                        # Store relative path for display/reference
                        filename=display_filename,
                        # Use standard Path.suffix
                        extension=fname_path.suffix,
                        url=doc_url, # Use URL from map
                        # Store the source directory name for context
                        # Use standard Path.name
                        source_dir=training_dir_path.name,
                    ),
                )
                nodes.extend(parser.get_nodes_from_documents([doc])) # Use extend
            except Exception as e:
                print(f"Error processing file {fname_path}: {e}", file=sys.stderr)
                continue # Skip problematic files

        if not nodes:
            print("Error: No valid documents could be processed to build the index.", file=sys.stderr)
            raise ValueError("Failed to build index due to lack of processable documents.")


        print(f"Indexing {len(nodes)} nodes...")
        index = VectorStoreIndex(nodes, show_progress=True)
        try:
            dname.parent.mkdir(parents=True, exist_ok=True)
            index.storage_context.persist(persist_dir=str(dname)) # Ensure path is string
            print(f"Saved new index to {dname}")
        except Exception as e:
            print(f"Error saving index to {dname}: {e}", file=sys.stderr)
            # Decide if we should raise here or just warn

    return index


# <<< ADD THESE FUNCTIONS >>>

def get_index_dir(data_subdir="training_data_aider"):
    """Helper to get the index directory path based on STANDALONE_RAG_VERSION."""
    # Use a dedicated cache directory for the standalone tool
    cache_base_dir = Path.home() / ".standalone_rag_cache"
    dname = cache_base_dir / ("index." + STANDALONE_RAG_VERSION)
    return str(dname) # Return as string path

def ask_question(question, data_subdir="training_data_aider"):
    """
    Performs a RAG query using the standalone help index.

    Args:
        question: The question to ask.
        data_subdir: The subdirectory containing the index data (used to find index).

    Returns:
        A formatted string containing the answer and retrieved documents, or an error string.
    """
    index_dir = get_index_dir(data_subdir)
    if not os.path.exists(index_dir):
        # Try building it if it doesn't exist? Or just error?
        # Let's try building it.
        print(f"Index not found at {index_dir}. Attempting to build...")
        try:
            # Ensure dependencies are met before trying to build
            if not install_dependencies_if_needed():
                 return "Error: Dependencies missing and could not be installed. Cannot build index."
            index = get_index() # This will build and save if missing
            if index is None:
                 return f"Error: Failed to build index. Check logs."
            print("Index built successfully.")
        except Exception as e:
            return f"Error: Failed to build index required for asking question: {e}"
        # If build succeeded, index_dir should now exist.

    # Configure embedding model (needed for loading too)
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    try:
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    except Exception as e:
        return f"Error initializing embedding model for query: {e}"


    try:
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context)
        # Configure retriever settings if needed, e.g., top_k
        retriever = index.as_retriever(similarity_top_k=5) # Retrieve top 5 docs for testing
        nodes = retriever.retrieve(question)
    except FileNotFoundError:
        # This case should be less likely now with the build attempt above
        return f"Error: Index directory not found at {index_dir} even after build attempt."
    except Exception as e:
        return f"Error loading index or retrieving documents: {e}"


    # Format the response similar to how aider's Help class might
    prompts = HelpPrompts() # Use the prompts from standalone_rag_help
    response = prompts.format_ask_response(question, nodes)
    return response

def retrieve_raw_context(question, top_k=5):
    """
    Retrieves raw text context relevant to the question from the index.

    Args:
        question (str): The question to query the index with.
        top_k (int): The number of top documents to retrieve.

    Returns:
        str: A string containing the concatenated text of the retrieved documents,
             or an error message string starting with "Error:".
    """
    index_dir = get_index_dir() # Assumes default index location
    if not os.path.exists(index_dir):
        # Attempt to build if missing
        print(f"Index not found at {index_dir}. Attempting to build...")
        try:
            if not install_dependencies_if_needed():
                 return "Error: Dependencies missing and could not be installed. Cannot build index."
            index = get_index()
            if index is None: return "Error: Failed to build index."
            print("Index built successfully.")
        except Exception as e:
            return f"Error: Failed to build index required for retrieval: {e}"

    # Configure embedding model (needed for loading)
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    try:
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    except Exception as e:
        return f"Error initializing embedding model for query: {e}"

    try:
        storage_context = StorageContext.from_defaults(persist_dir=index_dir)
        index = load_index_from_storage(storage_context)
        retriever = index.as_retriever(similarity_top_k=top_k)
        nodes = retriever.retrieve(question)
    except FileNotFoundError:
        return f"Error: Index directory not found at {index_dir} even after build attempt."
    except Exception as e:
        return f"Error loading index or retrieving documents: {e}"

    if not nodes:
        return "No relevant context found."

    # Concatenate the text content of the nodes
    context_text = "\n\n---\n\n".join([node.get_content().strip() for node in nodes])
    return context_text

# <<< END OF ADDED FUNCTIONS >>>


class Help:
    def __init__(self):
        # LlamaIndex settings (like embed_model) are now set globally in get_index
        # Ensure dependencies are checked before initializing
        # Note: install_dependencies_if_needed should ideally be called by the CLI entry point
        # before Help() is instantiated.

        # Initialize the index (loads or builds)
        self.index = get_index()
        if self.index is None:
             # Handle case where index creation failed critically
             raise RuntimeError("Failed to initialize or load the RAG index.")


        # Configure the retriever
        self.retriever = self.index.as_retriever(similarity_top_k=20)
        print("RAG helper initialized.")

    def ask(self, question):
        """Retrieves relevant documents and formats them for the user."""
        if not self.retriever:
            return "Error: Retriever not initialized."

        try:
            nodes = self.retriever.retrieve(question)
        except Exception as e:
            return f"Error during retrieval: {e}"

        context = f"# Question: {question}\n\n# Relevant docs:\n\n"

        if not nodes:
            context += "No relevant documents found.\n"
        else:
            for node in nodes:
                url = node.metadata.get("url", "")
                filename = node.metadata.get("filename", "unknown file")
                display_source = f'source="{filename}"'
                if url:
                    display_source += f' url="{url}"'

                context += f"<doc {display_source}>\n"
                context += node.text.strip() # Strip leading/trailing whitespace from node text
                context += "\n</doc>\n\n"

        return context.strip() # Strip trailing newline from final context
