import unittest
import pandas as pd

dfpath = getCSV('investments')
df = pd.read_csv(dfpath)

fileColumns = list(df.columns)

class TestFiltering(unittest.TestCase):
    def test_delColumns(self):
        result = ['name' ,'usd' ,'sector' ,'country' ]
        self.assertEqual(result, fileColumns)


if __name__ == "__main__":
    unittest.main()

