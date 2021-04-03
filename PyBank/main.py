#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#Pseudocode, Tally rows, add to variable for total months, add all the values from row[1] to a list and sum it, 
#Find the largest value in the list of row[1], add to variable for increase, same for decrease
import csv 
import os

#Value storage
total_months = 0
change = 0
total_sum = 0
avg_chg = 0
increasemax = 0
decreasemax = 0
starting_profit = 0 
final_profit = 0
initial_profit = 0

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
        total_months = len(row)
        print(total_months)
        
        #Sum column [1] in rows
        total_sum += int(row[1])
        #print(total_sum)

        

