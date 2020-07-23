# fileparse.py
import csv

def parse_csv(filename, select=None,types=None,has_headers=True, delimiter =None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows= csv(f,delimiter=delimiter)

        # Read the file headers
        headers = next(rows)

        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            
            if indices:
                row = [ row[index] for index in indices ]

            if types:
                 row = [func(val) for func, val in zip(types, row) ]

            if has_headers:
                    record = dict(zip(headers,row))
            else:
                record = tuple(row)

            record = dict(zip(headers, row))
            records.append(record)

    return records

    #if __name__ =
    records= parse_csv('Data/portfolio.csv', select=['name','shares'])
    print(records)
    records= parse_csv('Data/portfolio.csv', types=[str,int], select=['name','shares'])
    print(records)
    records= parse_csv('Data/portfolio.csv', types=[str,int], select=['name','shares'], has_headers =False)
    print(records)
    records= parse_csv('Data/portfolio.csv', types=[str,int], select=['name','shares'], has_headers =False, delimiter=' ')
    print(records)
