# pcost.py
#
# Exercise 1.27
import csv
import sys
def portfolio_cost(filename):
    """This function takes a filename as input, 
    reads the portfolio data in that file, 
    and returns the total cost of the portfolio as a float"""

    total_cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}')
                return 0.0
    return total_cost
        
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data/portfolio.csv'        
        
# cost=portfolio_cost(filename)
# print(f'Total cost: {cost:.2f}')