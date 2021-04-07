#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast - 

#* A complete list of candidates who received votes - values_count

#* The percentage of votes each candidate won

#* The total number of votes each candidate won - count votes by name

#* The winner of the election based on popular vote. -index, match names to vote counts,  build dictionary to match names to votes, 

#PSEUDOCODE tally votes from rows in list, values_count in row[2] to find candidate names, save to list,
#Append row[2] contents to list of candidates
# , 

import csv
import os

#Value storage
votes = []
votes_count = 0
sum_votes = set()
candidates = []
candidate_names = []
sum_candidates = 0
candidate_percent = 0
max_votes = ()
sumvote1 = set()
sumvote2 = []
sumvote3 = 0
sumvote4 = 0
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
        votes_count += 1
        votes = (row[2])
        #Get candidate names
        if votes in candidate_names: 
            candidates.append(row[2])
            candidate_names = dict.fromkeys(candidates)
        print(candidate_names)
            
        
        
        
        
#vote_analysis = os.path.join("Analysis", "budget_analysis.txt")
#with open(budget_analysis, 'w', newline='') as txtdoc:

    #txtdoc.write('Election Analysis\n')
    #txtdoc.write('---------------------------\n')
    #txtdoc.write('Total Votes: '+str(sum_votes))
    #txtdoc.write('---------------------------\n')
    #txtdoc.write('candidate1: ')
    #txtdoc.write('candidate2: '+increase_month +' $' +str(increasemax))
    #txtdoc.write('candidate3: ')
    #txtdoc.write('candidate4: ')
    #txtdoc.write('---------------------------\n')
    #txtdoc.write('Winner: '+decrease_month +' $' +str(decreasemax))
    #txtdoc.write('---------------------------\n')