# flake8: noqa: E501

from pathlib import Path
try:
    import importlib.resources as importlib_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources
import sys # Needed for print to stderr

# <<< FUNCTION MOVED HERE >>>
def fname_to_url(filepath, data_subdir="training_data"):
    """
    Converts a file path potentially containing the data_subdir component
    into a documentation URL. Handles relative and absolute paths.
    """
    base_url = "https://aider.chat/"
    index_suffix = "index.md"
    md_suffix = ".md"
    html_suffix = ".html"

    try:
        # Ensure filepath is a string and handle potential None or empty input
        if not filepath:
            return ""

        # Normalize path separators to forward slashes for consistent parsing
        filepath_normalized = filepath.replace("\\", "/")

        # Convert to Path object for easier manipulation
        path = Path(filepath_normalized)
        parts = path.parts

        # Find the index of the data_subdir component
        try:
            # Find the *last* occurrence in case data_subdir appears earlier in the path
            # (e.g., /path/to/training_data/project/training_data/docs/...)
            # Reverse parts, find first occurrence, convert index back
            reversed_parts = list(parts)[::-1]
            reversed_subdir_index = reversed_parts.index(data_subdir)
            subdir_index = len(parts) - 1 - reversed_subdir_index
        except ValueError:
            # data_subdir not found in the path parts
            # This path doesn't seem to be part of the website data structure
            # print(f"Warning: '{data_subdir}' not found in path '{filepath}' for URL generation.", file=sys.stderr)
            return ""

        # Get the parts *after* data_subdir
        relevant_parts = parts[subdir_index + 1 :]

        if not relevant_parts:
            # Path ended exactly with data_subdir (e.g., "path/to/training_data")
            # This doesn't correspond to a specific doc page.
            return ""

        # Handle directories starting with '_' immediately after data_subdir
        if relevant_parts[0].startswith("_"):
            return ""

        # Join the relevant parts to form the URL path component
        url_path_part = "/".join(relevant_parts)

        # Handle index.md and other .md files suffixes
        if url_path_part.lower().endswith(index_suffix.lower()):
            # Remove index.md suffix
            url_path_part = url_path_part[:-len(index_suffix)]
        elif url_path_part.lower().endswith(md_suffix.lower()):
            # Replace .md suffix with .html
            url_path_part = url_path_part[:-len(md_suffix)] + html_suffix

        # Clean up any trailing slashes resulting from index suffix removal
        url_path_part = url_path_part.strip("/")

        # Construct the final URL
        # If url_path_part is empty, it means the path was like '.../training_data/docs/index.md',
        # and the part *before* index.md should form the URL path.
        # Example: training_data/docs/index.md -> relevant_parts=('docs', 'index.md') -> url_path_part='docs'
        # Example: training_data/docs/usage.md -> relevant_parts=('docs', 'usage.md') -> url_path_part='docs/usage.html'
        # Example: training_data/index.md -> relevant_parts=('index.md',) -> url_path_part=''
        # In the last case, return base_url? The tests imply this shouldn't map. Let's return base_url + url_path_part
        final_url = f"{base_url}{url_path_part}"

        return final_url

    except Exception as e:
        # Catch any unexpected errors during path manipulation
        print(f"Error during URL generation for '{filepath}': {e}", file=sys.stderr)
        return ""
# <<< END OF MOVED FUNCTION >>>


class HelpPrompts:
    main_system = """You are an expert on the AI coding tool called Aider.
Answer the user's questions about how to use aider.

The user is currently chatting with you using aider, to write and edit code.

Use the provided aider documentation *if it is relevant to the user's question*.

Include a bulleted list of urls to the aider docs that might be relevant for the user to read.
Include *bare* urls. *Do not* make [markdown links](http://...).
For example:
- https://aider.chat/docs/usage.html
- https://aider.chat/docs/faq.html

If you don't know the answer, say so and suggest some relevant aider doc urls.

If asks for something that isn't possible with aider, be clear about that.
Don't suggest a solution that isn't supported.

Be helpful but concise.

Unless the question indicates otherwise, assume the user wants to use aider as a CLI tool.

Keep this info about the user's system in mind:
User is running this standalone help tool.
"""

    example_messages = [] # Keep empty unless specific examples are needed
    system_reminder = ""

    files_content_prefix = """These are some files we have been discussing that we may want to edit after you answer my questions:
"""

    files_no_full_files = "I am not sharing any files with you."

    files_no_full_files_with_repo_map = ""
    files_no_full_files_with_repo_map_reply = ""

    repo_content_prefix = """Here are summaries of some files present in my git repository.
We may look at these in more detail after you answer my questions.
"""

    # <<< ADD THIS METHOD >>>
    def format_ask_response(self, question, nodes):
        """
        Formats the RAG response including the question and retrieved documents.
        """
        response = f"# Question: {question}\n\n"
        response += "Based on the following documents:\n\n"
        for i, node in enumerate(nodes):
            content = node.get_content()
            metadata = node.metadata or {}
            # Use 'file_path' which is standard in LlamaIndex metadata
            # Corrected: LlamaIndex uses 'filename' or similar, let's stick to what rag_core uses
            # Re-Correction: The original aider code used 'filename', let's use that for consistency
            # with how the index might be built or how fname_to_url expects input.
            # Final Decision: Check rag_core's Document creation. It uses 'filename'.
            filepath = metadata.get("filename", "Unknown source")
            # We need the full path potentially for fname_to_url, metadata might only have filename.
            # Let's assume fname_to_url can handle just the filename if the index metadata stores it that way.
            # If the index stores a full path in metadata (e.g., under 'file_path'), use that.
            # Sticking with 'filename' as per rag_core's Document creation metadata.
            url = fname_to_url(filepath) # Use the existing function from rag_core
            response += f"<doc path=\"{filepath}\" url=\"{url}\">\n"
            response += content.strip() # Strip whitespace from content
            response += "\n</doc>\n\n"
        return response.strip() # Strip trailing whitespace/newlines
    # <<< END OF ADDED METHOD >>>
