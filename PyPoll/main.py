import os
import csv


csvpath = os.path.join(".", "Resources", "election_data.csv")
csvoutput = os.path.join(".", "analysis", "election_analysis.txt")

votes = 0
vote_count = []
candidate_list = []



with open(csvpath) as csvfile:
    print(csvpath)
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    
    for row in csvreader:
        votes = votes +1
        candidate = row[2]

        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidate_list.append(candidate)
            vote_count.append(1)

percentages = []
vote_winner = vote_count[0]
vote_winner_index = 0

for count in range(len(candidate_list)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > vote_winner:
        print(vote_winner)

winner = candidate_list[vote_winner_index]
percentages = [round (i,2) for i in percentages]

print()

poll_analysis = f'''
Election Results
---------------------
Total Votes: {votes}
---------------------
{candidate_list[count]}: {percentages[count]}% {vote_count[count]}
---------------------
Winner: {winner}
---------------------
'''

print(poll_analysis)

with open(csvoutput, 'w') as txt_file:
    txt_file.write(str(poll_analysis))