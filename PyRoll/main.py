#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

#* A complete list of candidates who received votes - values_count

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote. -

#PSEUDOCODE tally votes from rows in list, values_count in row[2] to find candidate names, save to list,
#Append row[2] contents to list of candidates
# , 

import csv
import os

#Value storage
votes = []
sum_votes = 0
candidates = []
candidate_names = []
sum_candidates = 0
candidate_percent = 0
max_votes = ()
sum_candidate1 = 0
sum_candidate2 = 0
sum_candidate3 = 0
sum_candidate4 = 0
winner = ()
#Path to election data.csv from Resources folder
data_csv = os.path.join("Resources", "election_data.csv")


#Open file
with open(data_csv, 'r') as datafile:
    csv_reader = csv.reader(datafile, delimiter=',')
    
    #Skip header
    csv_header = next(csv_reader)

    for row in csv_reader:
        #Tally votes
        sum_votes += 1
        #Get candidate names
        
        for i in votes:
            if i not in votes:
                candidate_names.append(i)
        #print(candidate_names)
        
        

