
# Allows to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..','Resources','budget_data.csv')

os.chdir(os.path.dirname(__file__))

# Open and read CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#create lists and set variable values
    months = []
    revenue = []
    month_count = 0
    max_profit = 0
    min_profit = 0
    deltas = []
    max_month = ""
    min_month = ""
    pre_revenue = 0

    for row in csvreader:
        
        #Determine total number of months
        month_count += 1
              
        #Add Profit / Losses
        revenue = float(row[1])
      
        #Determine total revenue 
        total_revenue += int(row[1])   

        #Calculate the monthly Profit/Loss changes
        delta = revenue - pre_revenue
        deltas.append(delta) 
        pre_revenue = revenue
        
        #Maximum Profit and Month
        if max_profit < delta:
            max_profit = delta
            max_month = row[0]
        #Minimum Profit and Month
        if min_profit > delta:
            min_profit = delta  
            min_month = (row[0])


    deltas=deltas[1:]
      average = round(sum(deltas)/len(deltas),2) 
    print(average)
    print(round(max_profit),(max_month), min_month, round(min_profit))

        
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}')
print(f'Total :  $ {total_revenue}')
print(f'Average Change:  $ {average}')
print(f'Greatest Increase in Profits: {max_month}  (${max_profit})')
print(f'Greatest Decrease in Profits: {min_month}  (${min_profit})')
print("```")


with open('Financial_Analysis.txt', 'w') as text:
    text.write("```text" + "\n")
    text.write('\nFinancial Analysis')
    text.write('\n----------------------------\n')
    text.write(f'Total Months: {month_count}\n')
    text.write(f'Total :  $ {total_revenue}\n')
    text.write(f'Average Change:  $ {average}\n')
    text.write(f'Greatest Increase in Profits: {max_month}  (${max_profit})\n')
    text.write(f'Greatest Decrease in Profits: {min_month}  (${min_profit})\n')
    text.write('\n```')


