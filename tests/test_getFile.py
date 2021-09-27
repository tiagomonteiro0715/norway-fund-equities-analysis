import unittest
import os

class TestgetFile(unittest.TestCase):
    def test_getCSV(self, fileName):
        result = os.path.join(os.getcwd(), fileName + ".csv")
        self.assertEqual(result, os.path.join(os.getcwd(), fileName + ".csv"))


if __name__ == "__main__":
    unittest.main()

