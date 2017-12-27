'''
    This module is responsible for sqlite queries. The implementation allows for "Singleton" logic to be implemented
'''

import pandas as pd
import sqlite3
import logging
from urllib.request import pathname2url

class Sqlite:
    connection = None
    connection_path = None

    def establish_connection(self, target):
        '''
        Method establishes a connection to a sqlite database or file. It only allows read only access to the target to
        make sure that no modification will accidentally be made
        :param target: The target sqlite database or file to connect to
        :return: None - Establishes a connection to the target database or file
        :except: FileNotFoundError - if target database or file does not exist
        '''
        if self.connection is None and self.connection_path is None:
            # The default mode of opening an sqlite db is 'rwc' (read-write-create)
            # Using a URI, we can specify a different mode instead; if we set it to rw, an exception is raised when
            # trying to connect to a non-existing database. We can set different modes when you set the flag uri=True
            # when connecting and pass in a file: URI, and add a mode=rw query parameter to the path:
            try:
                self.connection = sqlite3.connect('file:{}?mode=ro'.format(pathname2url(target)), uri=True)
            except sqlite3.OperationalError:
                logging.error('Target file or database: "{}" is missing'.format(target))
                raise FileNotFoundError
            self.connection_path = target
            logging.info('Established connection')
        else:
            logging.info('The requested connection already exists')


    def read_query_dataframe(self, target, query, index_col=None, coerce_float=True, params=None,
                   parse_dates=None, chunksize=None):
        '''

        :param target:
        :param query:
        :param index_col:
        :param coerce_float:
        :param params:
        :param parse_dates:
        :param chunksize:
        :return:
        '''
        try:
            self.establish_connection(target)

        except FileNotFoundError:
            return None
        df = pd.read_sql_query(query, self.connection, index_col=index_col, coerce_float=coerce_float, params=params,
                   parse_dates=parse_dates, chunksize=chunksize)
        return df

    def read_query_csv(self, target, query, index_col=None, coerce_float=True, params=None,
                   parse_dates=None, chunksize=None):
        '''

        :param target:
        :param query:
        :param index_col:
        :param coerce_float:
        :param params:
        :param parse_dates:
        :param chunksize:
        :return:
        '''
        df = self.read_query_dataframe(target, query, index_col=index_col, coerce_float=coerce_float, params=params,
                   parse_dates=parse_dates, chunksize=chunksize)
        csv_format = df.to_csv()
        return csv_format