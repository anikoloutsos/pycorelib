import unittest
from data.input import tsv_reader as reader


class TestSqliteReader(unittest.TestCase):
    def test_get_columns_names(self):
        reader.get_columns_names('O:/Projects/Mercari_Price_Suggestion/test.tsv')

if __name__ == '__main__':
    unittest.main()
