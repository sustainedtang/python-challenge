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
from collections import Counter
votes = []
votes_sum = 0
votes_count = []
candidates = []
candidate_names = []
votes1 = []
votes_percent = []
candi0 = 0
candi1 = 0
candi2 = 0
candi3 = 0

#Path to election data.csv from Resources folder
data_csv = os.path.join("Resources", "election_data.csv")


#Open file
with open(data_csv, 'r', newline= "") as datafile:
    csv_reader = csv.reader(datafile, delimiter=',')
    
    #Skip header
    csv_header = next(csv_reader)
    votes = list(csv_reader)
    #Tally votes
    votes_sum = len(votes) 
    print(votes_sum)
    for i in votes:
        if (i[2]) not in candidates:
            candidates.append(i[2])
    
    for row in votes:
        votes_count.append(row[2])

    #print(candidates[0], candidates[1], candidates[2], candidates[3])
    #Count votes from names             
    
    candi1sum = votes_count.count(candidates[0])

    candi2sum = votes_count.count(candidates[1])

    candi3sum = votes_count.count(candidates[2])

    candi4sum = votes_count.count(candidates[3])

    print(candidates[0], candidates[1], candidates[2], candidates[3])
  
  

  #Percent votes of total

    candi1per ='{:.3%}'.format(candi1sum / votes_sum)

    candi2per ='{:.3%}'.format(candi2sum / votes_sum)

    candi3per ='{:.3%}'.format(candi3sum / votes_sum)

    candi4per ='{:.3%}'.format(candi4sum / votes_sum)


    winner = max(set(votes_count), key = votes_count.count)

    #print the result 
    print('Election Results')
    print('--------------------------')
    print(f'Total Votes: {votes_sum}')
    print('--------------------------')
    print(f'{candidates[0]} : {candi1per} ({candi1sum})')
    print(f'{candidates[1]} : {candi2per} ({candi2sum})')
    print(f'{candidates[2]} : {candi3per} ({candi3sum})')
    print(f'{candidates[3]} : {candi4per} ({candi4sum})')
    print('--------------------------')
    print(f'Winner : {winner}')
    print('--------------------------')        
        
        
        
        
vote_analysis = os.path.join("vote_analysis.txt")
with open(vote_analysis, 'w', newline='') as txtdoc:

    txtdoc.write('Election Analysis\n')
    txtdoc.write('---------------------------\n')
    txtdoc.write(f'Total Votes: {votes_sum}')
    txtdoc.write('---------------------------\n')
    txtdoc.write(f'{candidates[0]} : {candi1per} ({candi1sum})\n')
    txtdoc.write(f'{candidates[1]} : {candi2per} ({candi2sum})\n')
    txtdoc.write(f'{candidates[2]} : {candi3per} ({candi3sum})\n')
    txtdoc.write(f'{candidates[3]} : {candi4per} ({candi4sum})\n')
    txtdoc.write('---------------------------\n')
    txtdoc.write(f'Winner : {winner}\n')
    txtdoc.write('---------------------------\n')