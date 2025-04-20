
import unittest
from unittest.mock import patch, call
import os
import sys
from pathlib import Path
import time

# --- Test Configuration ---
# Set this environment variable to 'true' to run these tests
RUN_TESTS_ENV_VAR = "RUN_LLM_INTEGRATION_TESTS"
# --- End Configuration ---

# Ensure the module under test can be imported
try:
    from standalone_rag_help import llm_conversation
    from standalone_rag_help.rag_core import (
        install_dependencies_if_needed,
        get_index,
        get_index_dir,
        retrieve_raw_context # Import for checking context
    )
except ImportError:
    # If running tests from project root, adjust path
    project_root = Path(__file__).parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from standalone_rag_help import llm_conversation
    from standalone_rag_help.rag_core import (
        install_dependencies_if_needed,
        get_index,
        get_index_dir,
        retrieve_raw_context
    )

def get_required_api_key_env_var(model_name):
    """Determine the likely required API key env var based on model name."""
    model_lower = model_name.lower()
    if "gpt-" in model_lower or "openai" in model_lower:
        return "OPENAI_API_KEY"
    elif "claude" in model_lower:
        return "ANTHROPIC_API_KEY"
    elif "gemini" in model_lower:
        return "GEMINI_API_KEY"
    elif "deepseek" in model_lower:
        return "DEEPSEEK_API_KEY"
    # Add other common providers as needed
    else:
        # Default or fallback if model provider is unclear
        print(f"Warning: Unrecognized model provider for '{model_name}'. Assuming OPENAI_API_KEY.", file=sys.stderr)
        return "OPENAI_API_KEY"

# Determine if tests should run
should_run_tests = os.environ.get(RUN_TESTS_ENV_VAR, "false").lower() == "true"
api_key_var = get_required_api_key_env_var(llm_conversation.LLM_MODEL)
api_key_present = api_key_var in os.environ

# Define skip reason
skip_reason = f"Skipping integration tests: Set {RUN_TESTS_ENV_VAR}=true ({os.environ.get(RUN_TESTS_ENV_VAR)=})and ensure {api_key_var=} is set. ({os.environ.get(api_key_var)=})"

@unittest.skipUnless(should_run_tests and api_key_present, skip_reason)
class TestLLMConversationIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Ensure dependencies and RAG index are ready."""
        print("\nSetting up Integration Test Class...")
        if not install_dependencies_if_needed():
            raise unittest.SkipTest("Required dependencies are not installed.")

        force_rebuild = os.environ.get("REBUILD_RAG_INDEX", "false").lower() == "true"
        if force_rebuild:
            print("REBUILD_RAG_INDEX set. Forcing index rebuild for integration tests.")

        index_dir = get_index_dir()
        try:
            print("Ensuring RAG index exists...")
            start_time = time.time()
            get_index(force_rebuild=force_rebuild)
            end_time = time.time()
            if not os.path.exists(index_dir):
                 raise FileNotFoundError(f"Index directory {index_dir} not found after get_index call.")
            print(f"Index ready at {index_dir} (Setup took {end_time - start_time:.2f}s)")
        except Exception as e:
            print(f"Failed to ensure index is ready for tests: {e}", file=sys.stderr)
            raise unittest.SkipTest(f"Failed to prepare index for tests: {e}")

    # Patch input/print and dependency check, but not LLM or RAG calls
    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('builtins.input', side_effect=['Hello assistant!', 'quit'])
    def test_basic_chat_integration(self, mock_input, mock_install_deps):
        """Test a basic chat interaction with a real LLM call."""
        print("\nRunning test_basic_chat_integration...")
        start_time = time.time()
        assistant_output = []

        def capture_print(*args, **kwargs):
            """Capture specific print calls."""
            output = " ".join(map(str, args))
            # Capture only the assistant's final response line
            if output.startswith("\nAssistant: "):
                assistant_output.append(output[len("\nAssistant: "):])
            # Print normally for debugging if needed
            # print(*args, **kwargs, file=sys.__stdout__) # Use original stdout

        with patch('builtins.print', side_effect=capture_print):
            try:
                llm_conversation.main()
            except SystemExit:
                pass # Expected exit due to 'quit' input

        end_time = time.time()
        print(f"test_basic_chat_integration finished in {end_time - start_time:.2f}s")

        # Assertions
        mock_install_deps.assert_called_once()
        self.assertEqual(mock_input.call_count, 2) # 'Hello assistant!', 'quit'

        # Check that we got *some* response from the assistant
        self.assertTrue(assistant_output, "Assistant did not produce any output.")
        response_text = assistant_output[0]
        print(f"  Assistant Response: {response_text[:100]}...") # Print truncated response
        self.assertNotIn("Error:", response_text, "Assistant response contained an error.")
        self.assertGreater(len(response_text), 5, "Assistant response seems too short.")

    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('builtins.input', side_effect=['/help What is aider?', 'quit'])
    def test_help_command_integration(self, mock_input, mock_install_deps):
        """Test the /help command with real RAG and LLM calls."""
        print("\nRunning test_help_command_integration...")
        start_time = time.time()
        assistant_output = []
        question = "What is aider?" # Match the input side_effect

        def capture_print(*args, **kwargs):
            output = " ".join(map(str, args))
            if output.startswith("\nAssistant: "):
                assistant_output.append(output[len("\nAssistant: "):])
            # print(*args, **kwargs, file=sys.__stdout__)

        # Retrieve context *outside* the main loop call to see what *should* be used
        # This helps make assertions more specific
        expected_context = retrieve_raw_context(question)
        print(f"  Retrieved context for assertion check (first 100 chars): {expected_context[:100]}...")
        self.assertFalse(expected_context.startswith("Error:"), "RAG retrieval failed during test setup.")

        with patch('builtins.print', side_effect=capture_print):
            try:
                llm_conversation.main()
            except SystemExit:
                pass

        end_time = time.time()
        print(f"test_help_command_integration finished in {end_time - start_time:.2f}s")

        # Assertions
        mock_install_deps.assert_called_once()
        self.assertEqual(mock_input.call_count, 2) # '/help ...', 'quit'

        self.assertTrue(assistant_output, "Assistant did not produce any output for /help.")
        response_text = assistant_output[0]
        print(f"  Assistant Response: {response_text[:100]}...")
        self.assertNotIn("Error:", response_text, "/help response contained an error.")
        self.assertGreater(len(response_text), 10, "/help response seems too short.")

        # Flexible check: Does the response contain keywords likely from the context?
        # Keywords should ideally come from the 'expected_context' retrieved above.
        # Example keywords based on likely Aider docs:
        keywords = ["aider", "tool", "code", "llm", "gpt", "edit", "git"]
        found_keywords = [kw for kw in keywords if kw in response_text.lower()]
        print(f"  Keywords found in response: {found_keywords}")
        self.assertGreater(len(found_keywords), 1, f"Expected keywords ({keywords}) not sufficiently found in response.")

    # <<< ADD THIS NEW TEST METHOD >>>
    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('builtins.input', side_effect=['/help Explain map layering in Zoho Analytics', 'quit'])
    def test_help_command_zoho_integration(self, mock_input, mock_install_deps):
        """Test the /help command with real RAG and LLM calls for Zoho content."""
        print("\nRunning test_help_command_zoho_integration...")
        start_time = time.time()
        assistant_output = []
        question = "Explain map layering in Zoho Analytics" # Match the input side_effect

        def capture_print(*args, **kwargs):
            output = " ".join(map(str, args))
            if output.startswith("\nAssistant: "):
                assistant_output.append(output[len("\nAssistant: "):])
            # print(*args, **kwargs, file=sys.__stdout__) # Uncomment for debug prints

        # Retrieve context *outside* the main loop call to see what *should* be used
        expected_context = retrieve_raw_context(question)
        print(f"  Retrieved context for assertion check (first 100 chars): {expected_context[:100]}...")
        self.assertFalse(expected_context.startswith("Error:"), "RAG retrieval failed during test setup for Zoho question.")
        # Check if the retrieved context actually contains Zoho specific terms
        self.assertIn("zoho", expected_context.lower(), "Retrieved context doesn't seem to contain Zoho content.")
        self.assertIn("layer", expected_context.lower(), "Retrieved context doesn't seem to contain 'layer'.")

        with patch('builtins.print', side_effect=capture_print):
            try:
                llm_conversation.main()
            except SystemExit:
                pass # Expected exit due to 'quit' input

        end_time = time.time()
        print(f"test_help_command_zoho_integration finished in {end_time - start_time:.2f}s")

        # Assertions
        mock_install_deps.assert_called_once()
        self.assertEqual(mock_input.call_count, 2) # '/help ...', 'quit'

        self.assertTrue(assistant_output, "Assistant did not produce any output for Zoho /help.")
        response_text = assistant_output[0]
        print(f"  Assistant Response: {response_text[:100]}...")
        self.assertNotIn("Error:", response_text, "Zoho /help response contained an error.")
        self.assertGreater(len(response_text), 20, "Zoho /help response seems too short.") # Expect a decent explanation

        # Flexible check: Does the response contain keywords likely from the Zoho map layering context?
        keywords = ["layer", "map", "geo", "zoho", "visualization", "chart", "add", "hide"] # Keywords from map-layering.md
        found_keywords = [kw for kw in keywords if kw in response_text.lower()]
        print(f"  Keywords found in response: {found_keywords}")
        # Require a reasonable number of relevant keywords
        self.assertGreater(len(found_keywords), 3, f"Expected keywords ({keywords}) not sufficiently found in Zoho response.")
    # <<< END OF NEW TEST METHOD >>>


if __name__ == "__main__":
    # Ensure environment variables are checked before running
    if not should_run_tests:
        print(skip_reason)
    elif not api_key_present:
         print(f"API Key environment variable '{api_key_var}' not found.")
         print(skip_reason)

    # Run tests only if conditions are met (redundant with skipUnless but good practice)
    if should_run_tests and api_key_present:
        unittest.main()
    else:
         # Exit gracefully if tests are skipped by environment variable
         sys.exit(0)
