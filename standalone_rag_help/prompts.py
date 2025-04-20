# flake8: noqa: E501

from pathlib import Path
try:
    import importlib.resources as importlib_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources
import sys # Needed for print to stderr

# <<< REMOVE fname_to_url FUNCTION DEFINITION ABOVE >>>

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
            # Get the filename (or path stored during indexing under 'filename' key)
            filepath = metadata.get("filename", "Unknown source")
            # Get the URL directly from metadata (populated from CSV during indexing under 'url' key)
            url = metadata.get("url", "") # Default to empty string if not found
            response += f"<doc path=\"{filepath}\" url=\"{url}\">\n"
            response += content.strip() # Strip whitespace from content
            response += "\n</doc>\n\n"
        return response.strip() # Strip trailing whitespace/newlines
    # <<< END OF ADDED METHOD >>>
