#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote.

import csv
import os

#Value storage
votes = []
total_votes = 0
candidates = []
count_candidates = 0
candidate_percent = 0
max_votes = ()

#Path to election data.csv from Resources folder
data_csv = os.path.join("Resources", "election_data.csv")
