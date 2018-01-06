import unittest
from data.input import sqlite_reader as reader
from system.utils import logger

class TestSqliteReader(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        logger.initialize()
        super().__init__(methodName)

    def test_read_tables_names(self):
        self.assertIsNotNone(reader.get_tables_names('O:/Projects/Data/database.sqlite'))
        #print(df[df['type'] == 'table'])
        #print(df.loc[1])
        #print (df)
    def test_read_fails_when_missing_file(self):
        '''
        Asserts that if the database is missing None will be returned
        :return:
        '''
        self.assertIsNone(reader.get_tables_names('NonExistingFile'))

    def test_sqlite_recursivly(self):
        target = 'O:/Projects/Data/database.sqlite'
        tables = reader.get_tables_names(target)
        print(tables)
        for table in tables:
            columns = (reader.get_columns_names(target, table))
            print(columns)
            for column in columns:
                print(column)
                print(reader.get_columns_data(target, table, column))


if __name__ == '__main__':
    unittest.main()
