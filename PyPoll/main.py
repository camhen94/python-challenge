import os
import csv

#Define the path to the election CSV file
election_data = os.path.join('/Users/Tuna/Desktop/GitHub_Repo/python-challenge/PyPoll/Resources/election_data.csv')

#Open CSV file for reading
with open(election_data) as csvfile:

    #Create CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Skip header row
    csv_header = next(csvreader)

    #Initialize variables to store total votes, candidates, winner and max voges
    total_votes = 0
    candidates = {}
    winner = ""
    max_votes = 0

    #Iterate through CSV file to increment total votes
    for row in csvreader:
        total_votes += 1    

        #Update candidate votes in the dictionary
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

#Print election results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

#Iterate through candidates to calculate and print their percentage of votes
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#Print winner to terminal
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Print results to text file
with open("/Users/Tuna/Desktop/GitHub_Repo/python-challenge/PyPoll/Analysis/analysis.txt", mode="wt") as output_file:#
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

