import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")
os.chdir(os.path.dirname(__file__))

#create lists and set variable values
total_votes = 0
candidate_row = []
candidates = []
vote_count = []
vote_percent = []

# Open and read CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
 
    for row in csvreader:
        # Count the total number of votes
        total_votes = total_votes + 1
        candidate_row.append(row[2])
       
    # list of unique candidates
    for x in set(candidate_row):
        candidates.append(x)
      
        # votes per candidate
        candidate_votes = candidate_row.count(x)
        vote_count.append(candidate_votes)

        # % votes per candidate
        vote_pct = (candidate_votes/total_votes)*100
        vote_percent.append(vote_pct)

     #determine elecation winner   
    win1 = max(vote_count)
    winner = candidates[vote_count.index(win1)]
    
print("```text")
print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")
for i in range(len(candidates)):
    print(candidates[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("----------------------------")
print(f'Winner: {winner} ')
print("----------------------------")
print("```")


with open('Election_Results.txt', 'w') as text:
    text.write("```text" + "\n")
    text.write('\nElection Analysis')
    text.write('\n----------------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write('\n----------------------------\n')
    for i in range(len(set(candidates))):
        text.write(candidates[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")\n")
    text.write('\n----------------------------\n')
    text.write(f'Winner: {winner} ')
    text.write('\n----------------------------\n')
    text.write('\n```')


#os.chdir(os.path.dirname(__file__))
# Set variable for output file
#output_file = os.path.join("exc_pybank.txt")

# Set variable for output file
#output_file = os.path.join("exc_pypoll.txt")


