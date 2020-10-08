import os
import csv
import numpy as np

bank_csv = os.path.join("Resources", "budget_data.csv")
analysis_path = os.path.join("Analysis", "analysis.txt")

#set value for initial number of months
total_months = 0
#set initial value for total profit/loss
total_change = 0
# set initial value for average change
average_change = 0
# set initial value for max daily increase
max_increase = 0
# set initial value for max daily decrease
max_decrease = 0
# create empty list for storing daily change values in to find average change
daily_changes = []

def bank_analysis(bank_data):
    global max_increase
    global max_decrease
    global total_change
    profit_loss = int(bank_data[1])
    # uncomment print to see if the values are all being read in corrently
    #print(profit_loss)

    if profit_loss >= max_increase:
        max_increase = profit_loss
    
    if profit_loss <= max_decrease:
        max_decrease = profit_loss

    total_change = total_change + profit_loss

    daily_changes.append(bank_data[1])

#function to find average of daily changes
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total = total + float(number)
    return total / length



with open(bank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
   
    for row in csv_reader:
        #profit_loss = int(bank_csv[1])
        total_months = total_months + 1
        bank_analysis(row)


new_avg = average(daily_changes)

print("Total months: " + str(total_months))
print("The total change was: $" + str(total_change))
print("The maximum monthly decrease was: $" + str(max_decrease))
print("The maximum monthly increase was: $" + str(max_increase))
print("The average monthly change was: $" + str(new_avg))

txtfile = open(analysis_path, "w+")
txtfile.write('\n' + " Total months: " + str(total_months))
txtfile.write('\n' + " The total change was: $" + str(total_change))
txtfile.write('\n' + " The maximum monthly decrease was: $" + str(max_decrease))
txtfile.write('\n' + " The maximum monthly increase was: $" + str(max_increase))
txtfile.write('\n' + " The average monthly change was: $" + str(new_avg))

txtfile.close
