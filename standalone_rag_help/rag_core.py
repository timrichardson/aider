#!/usr/bin/env python

import json
import os
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

# Import prompts to use the formatter and fname_to_url
from .prompts import HelpPrompts, fname_to_url


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


def get_package_files(package_name="standalone_rag_help", data_subdir="training_data"):
    """Yields Path objects for all markdown files within the package's data subdir."""
    try:
        package_data_root = importlib_resources.files(package_name) / data_subdir
        if not package_data_root.is_dir():
            print(f"Error: Data directory '{data_subdir}' not found in package '{package_name}'.", file=sys.stderr)
            return

        for path in package_data_root.rglob("*.md"):
            if path.is_file():
                # Yield the path relative to the package data root for consistency
                # and to match the structure expected by fname_to_url if needed.
                yield path
    except Exception as e:
        print(f"Error accessing package data files: {e}", file=sys.stderr)


def fname_to_url(filepath, data_subdir="training_data"):
    """Converts a file path within the packaged data to a documentation URL."""
    # This assumes the URL structure matches aider.chat based on the relative path
    # within the training_data directory.
    base_url = "https://aider.chat/"
    index = "index.md"
    md = ".md"

    # Convert to Path object for easier manipulation
    path = Path(filepath)

    # Find the data_subdir part in the path
    try:
        # Get parts relative to the assumed package data root
        # This requires knowing where get_package_files starts yielding from.
        # Assuming yield path gives the full path, we need to make it relative.
        # Let's refine get_package_files to yield relative paths or handle it here.

        # Re-evaluate: Assume filepath is the absolute path from Path.rglob
        # We need to find the part relative to the data_subdir root.
        package_data_root = importlib_resources.files("standalone_rag_help") / data_subdir
        relative_path = path.relative_to(package_data_root)
        relevant_parts = relative_path.parts

    except (ValueError, NameError, Exception) as e:
         print(f"Warning: Could not determine relative path for URL generation: {e}", file=sys.stderr)
         return "" # Can't determine relative path

    # Handle _includes directory (or similar non-content dirs)
    if relevant_parts and relevant_parts[0].lower().startswith("_"):
        return ""

    # Join the remaining parts
    url_path = "/".join(relevant_parts)

    # Handle index.md and other .md files
    if url_path.lower().endswith(index.lower()):
        url_path = url_path[: -len(index)]
    elif url_path.lower().endswith(md.lower()):
        url_path = url_path[: -len(md)] + ".html"

    # Ensure the URL ends correctly
    url_path = url_path.strip("/")

def get_index():
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

    index = None
    try:
        if dname.exists():
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


    if index is None:
        print("Building new RAG index...")
        parser = MarkdownNodeParser()

        nodes = []
        # Assume training_data data is packaged within standalone_rag_help/training_data
        # The actual markdown files need to be copied there during packaging/setup.
        # For development, you might place them there manually.
        packaged_files = list(get_package_files())
        if not packaged_files:
             print("Error: No documentation files found in package data.", file=sys.stderr)
             print("Please ensure the 'training_data' directory exists and contains markdown files.", file=sys.stderr)
             # Decide how to handle this - raise error or return None?
             # Raising an error might be better to indicate setup issue.
             raise FileNotFoundError("No documentation files found to build index.")


        for fname_path in packaged_files:
            # fname_path is now a Path object from get_package_files
            if any(fname_path.match(pat) for pat in exclude_website_pats):
                continue

            try:
                # Generate URL based on the path
                doc_url = fname_to_url(str(fname_path))

                doc = Document(
                    text=fname_path.read_text(encoding="utf-8"),
                    metadata=dict(
                        filename=fname_path.name,
                        extension=fname_path.suffix,
                        url=doc_url, # Use generated URL
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

def get_index_dir(data_subdir="training_data"):
    """Helper to get the index directory path based on STANDALONE_RAG_VERSION."""
    # Use a dedicated cache directory for the standalone tool
    cache_base_dir = Path.home() / ".standalone_rag_cache"
    dname = cache_base_dir / ("index." + STANDALONE_RAG_VERSION)
    return str(dname) # Return as string path

def ask_question(question, data_subdir="training_data"):
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
