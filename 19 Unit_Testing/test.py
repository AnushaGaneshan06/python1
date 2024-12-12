import unittest
import test_cap  # Import the module containing the function to test

# Define a test case class that inherits from unittest.TestCase
class Testcap(unittest.TestCase):

    # Define a test method using the standard naming convention `test_`
    def test_add(self):

        # Call the function from the imported module and store the result
        result = test_cap.add(10, 15)

        # Use an assertion to check if the result matches the expected value
        # ----------------
        # test case 1:
        self.assertEqual(result, 25)



# Standard condition to allow the test to run directly when the file is executed
if __name__ == "__main__":
    unittest.main()
