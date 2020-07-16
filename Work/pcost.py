# pcost.py
#
# Exercise 1.27

import csv
def portfolio_cost(filename):
    TC = 0.00
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                C = float(row[1])*float(row[2])
                TC += C
            except ValueError:
                print('Bad row:', row)
    return TC

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = portfolio_cost(filename)
print('Total cost:', cost)