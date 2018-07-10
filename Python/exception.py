# exception.py

import csv

def portfolio_cost(filename):
    '''
    Computes total shares*price for a CSV file
    '''
    
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:', err)
                continue
            
            total += row[2] * row[3]
        return total

total = portfolio_cost('data/portfolio.csv')
print('Total cost:', total)
