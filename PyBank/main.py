import os
import csv

#Define the path to the budget CSV file
budget_data = os.path.join('/Users/Tuna/Desktop/GitHub_Repo/python-challenge/PyBank/Resources/budget_data.csv')

#Open CSV file for reading
with open(budget_data) as csvfile:

    #Create CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Skip header row
    csv_header = next(csvreader)

    #Initialize lists to store months and profit/loss
    months = []
    profit_loss = []

    #Iterate through CSV file to calculate months and convert profit/loss to int and append to list
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

    #Calculate total months
    total_months = len(months)

    #Calculate monthly change and average change    
    monthly_changes = [profit_loss[i] - profit_loss[i - 1] for i in range(1,total_months)]
    average_change = sum(monthly_changes) / len(monthly_changes)

    #Calculate greatest increase and decrease in profits
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    #Calculate dates corresponding to the greatest increase and decrease
    increase_date = months[monthly_changes.index(greatest_increase) + 1]
    decrease_date = months[monthly_changes.index(greatest_decrease) + 1]

#Print results to terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: $ {average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

#Print results to text file
with open("/Users/Tuna/Desktop/GitHub_Repo/python-challenge/PyBank/analysis/analysis.txt", mode="wt") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${sum(profit_loss)}\n")
    output_file.write(f"Average Change: $ {average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")