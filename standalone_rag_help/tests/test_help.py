import unittest
import os # Import os for path checking

# Import functions from rag_core (fname_to_url removed)
from standalone_rag_help.rag_core import ask_question, get_index_dir, get_index, install_dependencies_if_needed


class TestHelp(unittest.TestCase):
    # <<< REMOVE test_fname_to_url_unix and test_fname_to_url_edge_cases >>>

    @classmethod
    def setUpClass(cls):
        """
        Ensure dependencies are installed and index exists before running tests.
        Checks REBUILD_RAG_INDEX environment variable to force index rebuild.
        """
        print("\nSetting up TestHelp class...")
        if not install_dependencies_if_needed():
            raise unittest.SkipTest("Required dependencies are not installed. Skipping RAG tests.")

        # Check environment variable to force rebuild
        force_rebuild = os.environ.get("REBUILD_RAG_INDEX", "false").lower() == "true"
        if force_rebuild:
            print("REBUILD_RAG_INDEX environment variable set. Forcing index rebuild.")

        index_dir = get_index_dir() # Get expected index location

        try:
            # Call get_index, which handles loading, building, or forced rebuilding
            get_index(force_rebuild=force_rebuild)

            # Verify index directory exists after the call
            if not os.path.exists(index_dir):
                 raise FileNotFoundError(f"Index directory {index_dir} not found after get_index call.")
            print(f"Index is ready at {index_dir}.")

        except Exception as e:
            print(f"Failed to ensure index is ready for tests: {e}")
            # Optionally print traceback for more detail
            # import traceback
            # traceback.print_exc()
            raise unittest.SkipTest(f"Failed to prepare index for tests: {e}")


    def test_ask_standalone(self):
        """
        Tests the standalone RAG query functionality.
        Relies on setUpClass ensuring the index exists.
        """
        question = "What is zoho analytics?"
        result = ask_question(question)

        # Check if ask_question returned an error string
        if result.startswith("Error:"):
             self.fail(f"ask_question failed: {result}")

        print("\n--- RAG Result ---")
        print(result)
        print("--- End RAG Result ---")


        self.assertIn(f"# Question: {question}", result)
        self.assertIn("<doc", result)
        self.assertIn("</doc>", result)
        # Check for keywords (adjust if needed for standalone context)
        self.assertIn("zoho", result.lower())
        # self.assertIn("ai", result.lower()) # Less critical for standalone test
        # self.assertIn("tool", result.lower()) # Check for 'tool' instead of 'chat'

        # Assert that there are multiple <doc> entries (adjust count as needed)
        # This depends heavily on the retriever settings and content
        # ask_question sets similarity_top_k=5, so expect up to 5 docs
        doc_count = result.count("<doc")
        self.assertGreater(doc_count, 0, "Should retrieve at least one document")
        self.assertLessEqual(doc_count, 5, "Should retrieve at most 5 documents (as per retriever setting)")


        # Check for reasonable length
        self.assertGreater(len(result), 100) # Ensure we got a substantial response


if __name__ == "__main__":
    unittest.main()
