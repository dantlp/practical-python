# report.py
import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = parse_csv(filename, select['name', 'shares', 'price'], types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = parse_csv(filename, has_headers=False, types=[str, float])
    prices = dict(prices)
    return prices

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
        
def print_report(report):
    # Output the report
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in report:
        print('%10s %10d %10.2f %10.2f' % row)

def portfolio_report(portfolio_filename,prices_filename):
    # Read data files and create the report data        
    portfolio = read_portfolio(portfolio_filename)
    prices    = read_prices(prices_filename)

    # Generate the report data
    report    = make_report_data(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ == "__main__":
        import sys
        
        if len(sys.argv) 1=2:
            print('Usage: python report.py <portfolio.csv> <prices.csv>')
        else:
            portfolio_report(sys.argv[1],sys.argv[2])
