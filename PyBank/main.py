import os
import csv

csvoutput = os.path.join(".","analysis", "budget_analysis.txt")
csvpath = os.path.join(".","Resources", "budget_data.csv" )

total_months = []

net_change = [] 

with open(csvpath) as csvfile:
    print(csvpath)
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)
    print(header)

    for row in csvreader:
        
        net_change.append(int(row[1]))
        total_months = len(total_months)

        print(total_months)
#     total_profit = 0
    
#     #Count number of months
#     for row in csvreader:
#         total_months += 1

#         total_profit = total_profit + int(row[1])   
        
#         average_change = 

# print(total_months)

# print(total_profit)

# Financial_Analysis = ('Total Months: ' + str(total_months))
 
# # print(Financial_Analysis)   





#  #Export output
# with open(csvoutput, 'w') as text_file:
#     text_file.write(Financial_Analysis)





