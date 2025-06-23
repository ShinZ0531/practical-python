# report.py
#
# Exercise 2.4

import csv
from pprint import pprint
def read_portfolio(filename: str) -> list:
    """Reads a portfolio from a CSV file.

    Args:
        filename (str): The name of the CSV file containing the portfolio data.

    Returns:
        list: A list of dictionaries, each representing a holding in the portfolio.
        Each dictionary contains 'name', 'shares', and 'price' keys.
    """

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                name = str(record['name'])
                shares = int(record['shares'])
                price = float(record['price'])
                result = {
                    'name': name,
                    'shares': shares,
                    'price': price
                }
                portfolio.append(result)
            except ValueError as e:
                print(f'Row {rowno}: Bad row: {row}')
                return []
    return portfolio

            
def read_prices(filename: str) -> dict:
    """Reads stock prices from a CSV file.

    Args:
        filename (str): The name of the CSV file containing stock prices.

    Returns:
        dict: A dictionary where keys are stock names and values are their prices.
    """

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # next(f)
        prices = {}
        for row in rows:
            if row:
                # print(row)
                name = row[0]
                price = float(row[1])
                prices[name] = price
    return prices

    
def calculate_profit(portfolio: list, prices: dict) -> float:
    # 收入+=持股数*（当前价格-买入价）
    # 根据portfolio去找price，key都是'name'
    # 对着solution看了一眼，不行，不能单纯的用 当前价格-买入价 计算
    # 这样缺少当前价格的股票就没算进去
    # 应该用 总收入-总支出 计算
    profit = 0.0
    for k in portfolio:
        # print (k)
        name = k['name']
        shares = k['shares']
        price = k['price']
        if name in prices:
            profit += shares * (prices[name] - price)
    return profit
def make_report(portfolio: list, prices: dict) -> list:
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{'-'*10} {'-'*10} {'-'*10} {'-'*10}')
    
    report = []
    for k in portfolio:
        name = str(k['name'])
        shares = int(k['shares'])
        old_price = float(k['price'])
        new_price = float(prices[name])
        change = new_price - old_price
        report.append((name, shares, old_price, change))
        price = '$'+f'{new_price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')
    return report
    
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')        