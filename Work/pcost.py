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
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                total_cost += float(row[1]) * float(row[2])
            # print(f'Total cost {total_cost:.2f}')
            return total_cost
    except FileNotFoundError:
        print(f'File {filename} not found.')
        return 0.0
    except ValueError as e:
        print(f'Error processing file {filename}: {e}')
        return 0.0
        
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'        
        
cost=portfolio_cost(filename)
print(f'Total cost: {cost:.2f}')