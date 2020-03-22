### PYPOLL ###
# Install modules
import os
import csv

output = open("elec_output.txt", "w")

# 1. GET FILE & DATA
# Link os to csv reader path
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# 2. CALCULATE THINGS
# Read each row of data after the header
    total_votes = 0
    candidate_name = " "
    candidate_current_votes = 0
    candidate_votes = {}
    best_cand_n = " "
    best_cand_p = 0

    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name in candidate_votes.keys():
            candidate_current_votes = candidate_votes[candidate_name]
        else:
            candidate_current_votes = 0
        candidate_current_votes = candidate_current_votes + 1
        candidate_votes[candidate_name] = candidate_current_votes
    print("Total Votes: " + str(total_votes))
    print("Total Votes: " + str(total_votes), file = output)

    for candidate_name in candidate_votes:
        pwon = round(int(candidate_votes[candidate_name]) / int(total_votes) * 100,2)
        print(candidate_name + ": " + str(pwon) + "% " + "(" + str(candidate_votes[candidate_name])+ ")")
        print(candidate_name + ": " + str(pwon) + "% " + "(" + str(candidate_votes[candidate_name])+ ")", file = output)
        if int(pwon) > best_cand_p:
            best_cand_n = candidate_name
            best_cand_p = pwon
    print("Winner: " + best_cand_n)
    print("Winner: " + best_cand_n, file = output)

output.close

