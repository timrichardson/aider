import os
import sys
from pathlib import Path

# Ensure the package directory is in the path if running as a script
script_dir = Path(__file__).parent.resolve()
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir.parent)) # Add parent dir (e.g., 'aider')

try:
    import litellm
    # Set default verbosity for litellm
    litellm.set_verbose = False
    # You might need to configure specific models, e.g., for Anthropic:
    # litellm.modify_params = True
except ImportError:
    print("Error: litellm is required for LLM interaction.")
    print("Please install it: pip install litellm")
    sys.exit(1)

# Import RAG functions AFTER potentially modifying sys.path
try:
    from standalone_rag_help.rag_core import retrieve_raw_context, install_dependencies_if_needed
except ImportError as e:
     print(f"Error importing RAG core: {e}")
     print("Ensure you are running this from the correct directory or have installed the package.")
     sys.exit(1)

# --- Configuration ---
# Set the LLM model to use (ensure it's configured in your environment, e.g., API keys)
# Example: Use OpenAI's gpt-3.5-turbo. Ensure OPENAI_API_KEY is set.
LLM_MODEL = os.environ.get("AIDER_MODEL", "gpt-3.5-turbo")
# --- End Configuration ---

# --- System Prompts ---
DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."
RAG_SYSTEM_PROMPT = """You are an expert assistant. Answer the user's question based *only* on the provided context documents.
If the context does not contain the answer, state that clearly.
Do not make up information or answer based on prior knowledge outside the context.
Be concise and directly answer the question using the context.
"""
# --- End System Prompts ---

def get_llm_response(messages, model_name):
    """Sends messages to the LLM and returns the response content."""
    try:
        print("...", end="", flush=True) # Indicate LLM call
        response = litellm.completion(
            model=model_name,
            messages=messages,
            stream=False, # Keep it simple for now
        )
        print("\r   \r", end="", flush=True) # Clear indicator
        # Extract content, handling potential variations in response structure
        if response.choices and response.choices[0].message and response.choices[0].message.content:
             return response.choices[0].message.content.strip()
        else:
             # Log the unexpected response structure for debugging
             print(f"\nWarning: Unexpected LLM response structure: {response}", file=sys.stderr)
             return "Error: Could not extract response content."

    except Exception as e:
        print("\r   \r", end="", flush=True) # Clear indicator
        # Attempt to get more specific error info from litellm exceptions if possible
        error_message = f"Error calling LLM ({model_name}): {e}"
        if hasattr(e, 'message'): # Some LiteLLM exceptions might have a message attribute
            error_message += f"\nDetails: {e.message}"
        print(f"\n{error_message}", file=sys.stderr)
        return f"Error: Failed to get response from LLM. Details: {e}"


def main():
    print("Initializing RAG Conversation...")
    # Ensure RAG dependencies are met before starting
    if not install_dependencies_if_needed():
         print("Failed to meet RAG dependencies. Exiting.", file=sys.stderr)
         sys.exit(1)

    print(f"Using LLM: {LLM_MODEL}")
    print("Type '/help <your question>' to query documentation, or just chat.")
    print("Type '/exit' or 'quit' to end.")

    conversation_history = []

    while True:
        try:
            user_input = input("\n> ")
        except EOFError:
            print("\nExiting.")
            break

        user_input_lower = user_input.lower()
        if user_input_lower in ["quit", "exit", "/exit", "/quit"]:
            print("Exiting.")
            break

        if not user_input.strip():
            continue

        messages_for_llm = []
        is_help_query = False

        if user_input.startswith("/help "):
            is_help_query = True
            question = user_input[len("/help "):].strip()
            if not question:
                print("Please provide a question after /help.")
                continue

            print("Retrieving context...")
            retrieved_context = retrieve_raw_context(question)

            if retrieved_context.startswith("Error:"):
                print(retrieved_context)
                continue # Skip LLM call if RAG failed

            # Prepare messages for RAG-based query
            messages_for_llm.append({"role": "system", "content": RAG_SYSTEM_PROMPT})
            # Add conversation history BEFORE the RAG context and question
            messages_for_llm.extend(conversation_history)
            # Add the special user message combining context and question
            messages_for_llm.append({
                "role": "user",
                "content": f"Context:\n---\n{retrieved_context}\n---\n\nQuestion: {question}"
            })

        else:
            # Prepare messages for regular chat query
            messages_for_llm.append({"role": "system", "content": DEFAULT_SYSTEM_PROMPT})
            messages_for_llm.extend(conversation_history)
            messages_for_llm.append({"role": "user", "content": user_input})

        # --- Call LLM ---
        assistant_response = get_llm_response(messages_for_llm, LLM_MODEL)
        print(f"\nAssistant: {assistant_response}")

        # --- Update History ---
        # Add the *original* user input and the assistant's response
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": assistant_response})

        # Optional: Limit history size to prevent context overflow
        # MAX_HISTORY_TURNS = 10 # Example limit
        # if len(conversation_history) > MAX_HISTORY_TURNS * 2:
        #     conversation_history = conversation_history[-(MAX_HISTORY_TURNS * 2):]


if __name__ == "__main__":
    # Check for API keys (example for OpenAI)
    if "OPENAI_API_KEY" not in os.environ and "gpt-" in LLM_MODEL:
         print("Warning: OPENAI_API_KEY environment variable not set.", file=sys.stderr)
         # Add checks for other providers (Anthropic, DeepSeek, etc.) as needed
    # if "ANTHROPIC_API_KEY" not in os.environ and "claude-" in LLM_MODEL:
    #      print("Warning: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)

    main()
