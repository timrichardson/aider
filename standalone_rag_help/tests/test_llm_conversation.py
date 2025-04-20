
import unittest
from unittest.mock import patch, MagicMock, call
import sys
import os

# Ensure the module under test can be imported
# This might require adjusting sys.path depending on how tests are run
try:
    from standalone_rag_help import llm_conversation
except ImportError:
    # If running tests from project root, adjust path
    import sys
    from pathlib import Path
    project_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(project_root))
    from standalone_rag_help import llm_conversation


class TestLLMConversation(unittest.TestCase):

    def setUp(self):
        """Reset conversation history before each test."""
        # We need to patch the global conversation_history inside the main function's scope
        # This is tricky. Instead, we'll test the arguments passed to the LLM mock,
        # which implicitly tests history handling.
        pass

    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('standalone_rag_help.llm_conversation.get_llm_response')
    @patch('builtins.input', side_effect=['Hello there', 'quit'])
    def test_regular_chat(self, mock_input, mock_get_llm, mock_install_deps):
        """Test a regular chat message without RAG."""
        mock_get_llm.return_value = "Hi! How can I help?"

        # Run the main loop until the 'quit' input is encountered
        with patch('builtins.print') as mock_print:
            try:
                llm_conversation.main()
            except SystemExit: # Catch sys.exit called by install_deps failure simulation if needed
                 pass # Or assert specific exit code if testing that path

        # Assertions
        mock_install_deps.assert_called_once()

        # Check call to get_llm_response
        expected_messages = [
            {"role": "system", "content": llm_conversation.DEFAULT_SYSTEM_PROMPT},
            # No history on the first turn
            {"role": "user", "content": "Hello there"}
        ]
        mock_get_llm.assert_called_once_with(expected_messages, llm_conversation.LLM_MODEL)

        # Check output printed
        mock_print.assert_any_call("\nAssistant: Hi! How can I help?")

    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('standalone_rag_help.llm_conversation.retrieve_raw_context') # Target where it's used
    @patch('standalone_rag_help.llm_conversation.get_llm_response')
    @patch('builtins.input', side_effect=['/help What is RAG?', 'quit'])
    def test_help_command_success(self, mock_input, mock_get_llm, mock_retrieve_context, mock_install_deps):
        """Test the /help command with successful RAG retrieval."""
        mock_retrieve_context.return_value = "RAG means Retrieval-Augmented Generation."
        mock_get_llm.return_value = "Based on the context, RAG is Retrieval-Augmented Generation."

        with patch('builtins.print') as mock_print:
             try:
                 llm_conversation.main()
             except SystemExit:
                  pass

        # Assertions
        mock_install_deps.assert_called_once()
        mock_retrieve_context.assert_called_once_with("What is RAG?")

        # Check call to get_llm_response
        expected_messages = [
            {"role": "system", "content": llm_conversation.RAG_SYSTEM_PROMPT},
            # No history on the first turn
            {"role": "user", "content": "Context:\n---\nRAG means Retrieval-Augmented Generation.\n---\n\nQuestion: What is RAG?"}
        ]
        mock_get_llm.assert_called_once_with(expected_messages, llm_conversation.LLM_MODEL)

        # Check output printed
        mock_print.assert_any_call("\nAssistant: Based on the context, RAG is Retrieval-Augmented Generation.")

    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('standalone_rag_help.llm_conversation.retrieve_raw_context') # Target where it's used
    @patch('standalone_rag_help.llm_conversation.get_llm_response')
    @patch('builtins.input', side_effect=['/help What is RAG?', 'quit'])
    def test_help_command_rag_error(self, mock_input, mock_get_llm, mock_retrieve_context, mock_install_deps):
        """Test the /help command when RAG retrieval returns an error."""
        mock_retrieve_context.return_value = "Error: Index not found."

        with patch('builtins.print') as mock_print:
             try:
                 llm_conversation.main()
             except SystemExit:
                  pass

        # Assertions
        mock_install_deps.assert_called_once()
        mock_retrieve_context.assert_called_once_with("What is RAG?")
        mock_get_llm.assert_not_called() # LLM should not be called if RAG fails

        # Check error output printed
        mock_print.assert_any_call("Error: Index not found.")

    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('litellm.completion') # Mock the underlying litellm call inside get_llm_response
    @patch('builtins.input', side_effect=['Tell me a joke', 'quit'])
    def test_llm_call_error(self, mock_input, mock_litellm_completion, mock_install_deps):
        """Test when the call to the LLM fails."""
        mock_litellm_completion.side_effect = Exception("LLM API Error")

        with patch('builtins.print') as mock_print:
             try:
                 llm_conversation.main()
             except SystemExit:
                  pass

        # Assertions
        mock_install_deps.assert_called_once()
        mock_litellm_completion.assert_called_once() # Ensure litellm was called

        # Check error output printed (stderr is harder to capture reliably with patch)
        # Instead, check that the main print function printed the error message returned by get_llm_response
        mock_print.assert_any_call("\nAssistant: Error: Failed to get response from LLM. Details: LLM API Error")


    @patch('standalone_rag_help.llm_conversation.install_dependencies_if_needed', return_value=True)
    @patch('standalone_rag_help.llm_conversation.get_llm_response')
    @patch('builtins.input', side_effect=['First message', 'Second message', 'quit'])
    def test_history_management(self, mock_input, mock_get_llm, mock_install_deps):
        """Test that conversation history is passed correctly."""
        # Define responses for the two turns
        mock_get_llm.side_effect = [
            "Response to first.",
            "Response to second."
        ]

        with patch('builtins.print') as mock_print:
             try:
                 llm_conversation.main()
             except SystemExit:
                  pass

        # Assertions
        self.assertEqual(mock_get_llm.call_count, 2)

        # Check call for the FIRST message
        first_call_args = mock_get_llm.call_args_list[0][0][0] # Gets the 'messages' arg from first call
        expected_first_messages = [
            {"role": "system", "content": llm_conversation.DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": "First message"}
        ]
        self.assertEqual(first_call_args, expected_first_messages)

        # Check call for the SECOND message (should include history)
        second_call_args = mock_get_llm.call_args_list[1][0][0] # Gets the 'messages' arg from second call
        expected_second_messages = [
            {"role": "system", "content": llm_conversation.DEFAULT_SYSTEM_PROMPT},
            {"role": "user", "content": "First message"},
            {"role": "assistant", "content": "Response to first."},
            {"role": "user", "content": "Second message"}
        ]
        self.assertEqual(second_call_args, expected_second_messages)

        # Check outputs printed
        mock_print.assert_any_call("\nAssistant: Response to first.")
        mock_print.assert_any_call("\nAssistant: Response to second.")


if __name__ == "__main__":
    unittest.main()
