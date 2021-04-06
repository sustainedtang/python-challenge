#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#Pseudocode, Tally rows, add to variable for total months, add all the values from row[1] to a list and sum it, 
#Find the largest/smallest value in the list of row[1], add to variable for increase, same for decrease
#Use min max functions to find values, use value to find index for month name. Export print. 
import csv 
import os

#Value storage
count_months = 0
months = []
profit_change = 0
total_profits = []
sum_profits = 0
avg_change = 0
increasemax = 0
decreasemax = 0
profit_change_list = []

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")



#Open file 
with open(budget_csv, 'r',) as budgetfile:
    
    csv_reader = csv.reader(budgetfile, delimiter=',')
    #print(csv_reader)  
    #Skip Header
    csv_header = next(csv_reader)
    #print(csv_header)
    
    for row in csv_reader:
        
        #Tally months from rows
        count_months += 1
        #Create list of months
        months.append(row[0])
        #Shortcut for row[1]
        current_profit = (int(row[1]))
        #Sum column [1] 
        total_profits.append(current_profit)
        sum_profits = (sum(total_profits))
        #Set previous month's profit to current profit value
        last_month = 0
        
        if count_months == 1:
            last_month = current_profit
            continue
        else:
            profit_change = current_profit - last_month
            
            profit_change_list.append(profit_change)
            
            profit_change = current_profit
        
#Calculations for average
average_change = round(((sum(profit_change_list))/count_months - 1), 2)

#min/max profit change
increasemax = max(profit_change_list)
decreasemax = min(profit_change_list)

increaseindex = profit_change_list.index(increasemax)
decreaseindex = profit_change_list.index(decreasemax)

increase_month = months[increaseindex]
decrease_month = months[decreaseindex]


print('Financial Analysis\n')
print('---------------------------')
print('Total Months: '+str(count_months))
print('Total: $'+str(sum_profits))
print('Average Change: '+str(average_change))
print('Greatest Increase in Profits: '+increase_month +' $' +str(increasemax))
print('Greatest Decrease in Losses: '+decrease_month +' $' +str(decreasemax))

budget_analysis = os.path.join("Analysis", "budget_analysis.txt")
with open(budget_analysis, 'w', newline='') as txtdoc:

    txtdoc.write('Financial Analysis\n')
    txtdoc.write('---------------------------\n')
    txtdoc.write('Total Months: '+str(count_months))
    txtdoc.write('Total: $'+str(sum_profits))
    txtdoc.write('Average Change: '+str(average_change))
    txtdoc.write('Greatest Increase in Profits: '+increase_month +' $' +str(increasemax))
    txtdoc.write('Greatest Decrease in Losses: '+decrease_month +' $' +str(decreasemax))
