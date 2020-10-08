import os
import csv
import pandas as pd

election_csv = os.path.join("Resources", "election_data.csv")
analysis_path = os.path.join("Analysis", "analysis.txt")

#df=pd.read_csv(election_csv)
#print(df.groupby(['Candidate'],as_index=False).count())

#print(df.count())

candidates = []

#candidate dictionary for vote_tally
candidate_dict = {}

total_count = 0
# tally the total number of votes excluding the header row
def vote_counter():
    #call global variable
    global total_count
    #open and read file
    with open(election_csv) as election:
        
        reader = csv.reader(election, delimiter=",")

        for row in reader:
            #ignore header row
            if row[0] == 'Voter ID':
                pass
            else:
                total_count = total_count + 1
    return total_count

# create a list of candidates in the election
def candidates_list():
    
    global candidates

    with open(election_csv) as election:
        reader = csv.reader(election, delimiter=",")
        #skip header row
        next(reader)
        #add candidates if they are not already on the list
        for row in reader:
            if row[2] not in candidates:
                candidates.append(row[2])
            else:
                pass
    return candidates


# get a tally of votes and percent of votes for each candidate
def vote_tally():
    global candidate_dict
    global total_count
    #add candidates to candidate dictionary
    for candidate in candidates:
        candidate_dict[candidate] = [0,0]

    with open(election_csv) as tally:
        reader = csv.reader(tally, delimiter=",")
        next(reader)
        for row in reader:
            for key, value in candidate_dict.items():

                if key == row[2]:
                    value[1] = value[1] + 1
                    value[0] = round(((value[1] / total_count) * 100), 1)
                else:
                    pass
    return candidate_dict
#find the winner of the election
winner = "none"
def find_winner():
    #initialize leader variable 
    leader = 0
    global winner

    for key, value in candidate_dict.items():

        if value[1] > leader:
            leader = value[1]
            winner = key
        else:
            pass
    return winner            


#run and print results
vote_counter()
print("The total votes were: " + str(total_count))
candidates_list()
print("Candidates in the election: " + str(candidates))
vote_tally()
print("The % and total votes for each candidate were: " + str(candidate_dict))
find_winner()
print("And the winner was: " + str(winner) + "!")

#print analysis to text file
a = open(analysis_path, "w+")
a.write('Election Voting Results')
a.write('\n' + ('-' * 25))
a.write('\n' + 'Total Votes: ' + str(total_count))
a.write('\n' + ('-' * 25))
for key, value in candidate_dict.items():
    a.write('\n' + key + ': ' + str(value[0]) + '% (' + str(value[1])+ ')')
a.write('\n' + ('-' * 25))
a.write('\n' + 'Winner: ' + winner)
a.write('\n' + ('-' * 25))
