# pcost.py
#
# Exercise 1.27
Cost = 0
with open('portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        TC= float(row[1]) * float(row[2])
        Cost += TC
print('Total Cost')
print(Cost)