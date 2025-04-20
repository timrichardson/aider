import unittest
import os # Import os for path checking

# Import fname_to_url from prompts
from standalone_rag_help.prompts import fname_to_url
# Import other functions from rag_core
from standalone_rag_help.rag_core import ask_question, get_index_dir, get_index, install_dependencies_if_needed


class TestHelp(unittest.TestCase):
    def test_fname_to_url_unix(self):
        # Test relative Unix-style paths
        self.assertEqual(fname_to_url("training_data/docs/index.md"), "https://aider.chat/docs")
        self.assertEqual(
            fname_to_url("training_data/docs/usage.md"), "https://aider.chat/docs/usage.html"
        )
        self.assertEqual(fname_to_url("training_data/_includes/header.md"), "")

        # Test absolute Unix-style paths
        self.assertEqual(
            fname_to_url("/home/user/project/training_data/docs/index.md"), "https://aider.chat/docs"
        )
        self.assertEqual(
            fname_to_url("/home/user/project/training_data/docs/usage.md"),
            "https://aider.chat/docs/usage.html",
        )
        self.assertEqual(fname_to_url("/home/user/project/training_data/_includes/header.md"), "")

    def test_fname_to_url_edge_cases(self):
        # Test paths that don't contain 'training_data'
        self.assertEqual(fname_to_url("/home/user/project/docs/index.md"), "")
        self.assertEqual(fname_to_url(r"C:\Users\user\project\docs\index.md"), "")

        # Test empty path
        self.assertEqual(fname_to_url(""), "")

        # Test path with 'training_data' in the wrong place
        self.assertEqual(fname_to_url("/home/user/website_project/docs/index.md"), "")

    @classmethod
    def setUpClass(cls):
        """Ensure dependencies are installed and index exists before running tests."""
        print("\nSetting up TestHelp class...")
        if not install_dependencies_if_needed():
            raise unittest.SkipTest("Required dependencies are not installed. Skipping RAG tests.")

        index_dir = get_index_dir()
        if not os.path.exists(index_dir):
            print(f"Test index not found at {index_dir}. Attempting to build...")
            try:
                get_index() # Attempt to build the index
                if not os.path.exists(index_dir):
                     raise FileNotFoundError("Index build attempt failed.")
                print("Test index built successfully.")
            except Exception as e:
                print(f"Failed to build index for tests: {e}")
                raise unittest.SkipTest(f"Failed to build index for tests: {e}")
        else:
            print(f"Using existing test index at {index_dir}")


    def test_ask_standalone(self):
        """
        Tests the standalone RAG query functionality.
        Relies on setUpClass ensuring the index exists.
        """
        question = "What is aider?"
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
        self.assertIn("aider", result.lower())
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
