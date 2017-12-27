'''
    Module handles and manipulates all requests that are sqlite specific
    List of methods:
        get_tables_names
        get_columns_names
        get_column_data
'''
from data.dbhelpers.Sqlite import Sqlite
import logging


def get_tables_names(target, index_col=None, coerce_float=True, params=None,
                   parse_dates=None, chunksize=None):
    '''
    Parameters
    ----------
    target : string, target file or database to retrieve tables from
    index_col : string or list of strings, optional, default: None
        Column(s) to set as index(MultiIndex).
    coerce_float : boolean, default True
        Attempts to convert values of non-string, non-numeric objects (like
        decimal.Decimal) to floating point. Useful for SQL result sets.
    params : list, tuple or dict, optional, default: None
        List of parameters to pass to execute method.  The syntax used
        to pass parameters is database driver dependent. Check your
        database driver documentation for which of the five syntax styles,
        described in PEP 249's paramstyle, is supported.
        Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}
    parse_dates : list or dict, default: None
        - List of column names to parse as dates.
        - Dict of ``{column_name: format string}`` where format string is
          strftime compatible in case of parsing string times, or is one of
          (D, s, ns, ms, us) in case of parsing integer timestamps.
        - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
          to the keyword arguments of :func:`pandas.to_datetime`
          Especially useful with databases without native Datetime support,
          such as SQLite.
    chunksize : int, default None
        If specified, return an iterator where `chunksize` is the number of
        rows to include in each chunk.

    Returns
    -------
    list, default None
        Contains the names of the tables associated with the specific database
    '''
    df = Sqlite().read_query_dataframe(target, 'select * from sqlite_master', index_col=index_col,
                                       coerce_float=coerce_float, params=params, parse_dates=parse_dates,
                                       chunksize=chunksize)
    if df is None:
        logging.warning('Query returned an empty DataFrame. Returning None')
        return None
    else:
        tables_df = df[df['type'] == 'table']
        return tables_df.name.values.tolist()


def get_columns_names(target, table, index_col=None, coerce_float=True, params=None,
                   parse_dates=None, chunksize=None):
    '''

    :param target:
    :param table:
    :param index_col:
    :param coerce_float:
    :param params:
    :param parse_dates:
    :param chunksize:
    :return:
    '''
    df = Sqlite().read_query_dataframe(target, 'pragma table_info(\'{}\')'.format(table), index_col=index_col, coerce_float=coerce_float, params=params,
                   parse_dates=parse_dates, chunksize=chunksize)
    return df.name.values.tolist()[1:]


def get_columns_data(target, table, columns, index_col=None, coerce_float=True, params=None,
                     parse_dates=None, chunksize=None):
    if isinstance(columns, str):
        columns_string = columns
        logging.info('Provided columns as string: ' + columns)
    elif isinstance(columns, list):
        columns_string = ",".join(columns)
        logging.info('Provided columns as list, each element of the list is considered as a separate column of the query'
                     ': ' + columns)

    df = Sqlite().read_query_dataframe(target, 'select {} from {}'.format(columns_string, table), index_col=index_col,
                                       coerce_float=coerce_float, params=params,
                                       parse_dates=parse_dates, chunksize=chunksize)
    return df.values.tolist()