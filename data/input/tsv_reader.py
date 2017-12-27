import csv
import pandas as pd

def get_columns_names(target, encoding='utf-8'):
    with open(target, 'r', encoding=encoding) as tsv:
        tsvin = csv.reader(tsv, delimiter='\t')
        #        print (tsvin.next())
        headers = next(tsvin)
    print(headers)
    return headers

def get_column_data(target, *columns):
    pd.read_csv(target, delimiter='\t',)
