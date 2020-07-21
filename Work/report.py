# report.py
#
# Exercise 2.4

import csv
def read_portfolio(filename):
    'Read in the holdings from a Portfolio'''
    portfolio = []
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding =   {'name': row[0],
                        'shares': int(row[1]),
                        'price': float(row[2])
                        }
            portfolio.append(holding)    

    return portfolio

def read_prices(filename):
    prices ={}

    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows :
        try:
            prices[row[0]] = float(row[1])
        except IndexError:
            pass

    return prices

def make_report(portfolio,prices):
    x=[]
    for s in portfolio:
        cost = prices[s['name']]
        Gainloss = cost - s['price']
        summary= (s['name'], s['shares'], cost, Gainloss)
        #tupple to recollect all data
        x.append(summary)
    return x

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)
total_cost = 0.0
current_value = 0.0
print('Name','#shares','Price','Gain/Loss')
for q in report:
    print(q)

#print('Total cost', total_cost)
#print('Current value:', current_value)
#print('Gain/Loss:', current_value - total_cost)
