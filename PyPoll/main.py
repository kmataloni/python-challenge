import os
import csv


csvpath = os.path.join(".", "Resources", "election_data.csv")
csvoutput = os.path.join(".", "Resources", "election_analysis.txt")

total_votes = 0
candidate_list = []
vote_percent = /total_votes

print(csvpath)
with open(csvpath) as csvfile:
    print(csvpath)
    csvreader = csv.reader(csvfile)

    header = next(csvreader)
    print(header)

#     for row in csvreader:
#         total_votes += 1
#         candidate_list = str([2])

#         print(total_votes)

#         print(candidate_list)



