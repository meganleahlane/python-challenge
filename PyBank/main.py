# Install modules
import os
import csv

output = open("bank_output.txt", "w")

# 1. GET FILE & DATA
# Link os to csv reader path
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# 2. CALCULATE THINGS

    # Read each row of data after the header
    total_months = 0
    net_total = 0
    prev_month = 0
    diff = 0
    total_diff = 0
    best = 0
    worst = 0
    best_month = " "
    worst_month = " "


    for row in csvreader:
        print(row)
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        if total_months == 1:
            prev_month = row[1]
        diff = int(row[1]) - int(prev_month)
        if diff > best:
            best = diff
            best_month = row[0]
        if diff < worst:
            worst = diff
            worst_month = row[0]
        total_diff = total_diff + diff
        prev_month = row[1]
        
    print("Total Months: " + str(total_months))
    print("Total Months: " + str(total_months), file = output)
    print("Total: " + "$" + str(net_total))
    print("Total: " + "$" + str(net_total), file = output)
    avg_diff = round(total_diff / (total_months - 1), 2)
    print("Average Change: " + "$" + str(avg_diff))
    print("Average Change: " + "$" + str(avg_diff), file = output)
    print("Greatest Increase in Profits: " + str(best_month) + " " + "(" + "$" + str(best) + ")")
    print("Greatest Increase in Profits: " + str(best_month) + " " + "(" + "$" + str(best) + ")",file = output)
    print("Greatest Decrease in Profits: " + str(worst_month) + " " + "(" + "$" + str(worst) + ")")
    print("Greatest Decrease in Profits: " + str(worst_month) + " " + "(" + "$" + str(worst) + ")", file = output)

output.close