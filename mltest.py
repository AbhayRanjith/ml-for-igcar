import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib as mpl
import seaborn as sb
import csv

filename  = "train.csv"

fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    fields = next(csvreader)
    
    for row in csvreader:
        rows.append(row)
        
    print("Total no. of rows: %d" % (csvreader.line_num))
    
print('Field names are:' + ', '.join(field for field in fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" "), 
    print('\n')