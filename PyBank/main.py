import os
import csv

csvoutput = os.path.join(".", "analysis", "budget_analysis.txt")
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# initializing variables
total_months = 1

total_profit = 0

change = 0

net_change = 0

average_change = 0

greatest_increase = ["", 0]

greatest_decrease = ["", 9999999999999]

#reading csv file
with open(csvpath) as csvfile:
    print(csvpath)
    csvreader = csv.reader(csvfile)

    # Read the header row
    header = next(csvreader)
    print(header)
    
    first_row = next(csvreader)
    print(first_row)

    # Add January into total profit
    total_profit += int(first_row[1])
    # Define previous month
    previous_month = (first_row[1])

    # Count number of months
    for row in csvreader:
        total_months += 1
        
        total_profit = total_profit + int(row[1])   
        

        # Difference between current month and previous month

        change = int(row[1]) - int(previous_month)
        
        # increment previous month January becomes February
        previous_month = row[1]
        
        # print(change)

        net_change +=change

        if  change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        
        if  change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change


    average_change = net_change / (total_months - 1)
   

# # print(total_months)

# # print(total_profit)

Financial_Analysis = f'''
    Financial Analysis
    -----------------------
    Total Months: {total_months}
    Total: ${total_profit}
    Average Change: {round(average_change,2)}
    Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}
    Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}
    '''


print(Financial_Analysis)   




 #Export output
with open(csvoutput, 'w') as txt_file:
    txt_file.write(str(Financial_Analysis))


