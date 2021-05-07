import os
import csv


csvpath = os.path.join(".","Resources", "budget_data.csv" )
print(csvpath)
with open(csvpath) as csvfile:
    print(csvpath)
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)
    print(header)

    total_months = 0
    #print(total_months)
    
    #Count number of months
    for row in csvreader:
        total_months += 1


print(total_months)

Financial_Analysis = ('Total Months' + str(total_months)/n)

    #f"Financial Analysis"
    #f"----------------------"
   




print(Financial_Analysis)   
    