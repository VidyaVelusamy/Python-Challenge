import os
import csv


Election_data = os.path.join("Resources","election_data.csv")


print("Election Results")
print("----------------------------")

with open(Election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    ballotID =[]
    Candidate=[]
    Candidate_list =[]
    winner=0
    
   
    csv_reader.__next__()
    for row in csv_reader:
        ballotID.append(row[0])
        Candidate.append(row[2])
    
    for i in Candidate:
        if i not in Candidate_list:
            Candidate_list.append(i)
    
    print(f"Total Votes:{len(ballotID)}")
    print("----------------------------")
output_path = os.path.join("C:/Users/vidya/pythonassignment/Python-Challenge/PyPoll", "Analysis", "Election_results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes:{len(ballotID)}\n")
    file.write("----------------------------\n")
    for i in range(len(Candidate_list)):

        total_votes = sum(1 for Name in Candidate if Name == Candidate_list[i])
        if total_votes > winner:
            winner = total_votes
            winnername=Candidate_list[i]
        percentage = total_votes/len(ballotID)*100
        print(f"{Candidate_list[i]}:{round(percentage,3)}% {total_votes} ")
        file.write(f"{Candidate_list[i]}:{round(percentage,3)}% {total_votes}\n")
    print("----------------------------\n")
    print(f"Winner :{winnername}\n")
    file.write("----------------------------\n")
    file.write(f"Winner :{winnername}\n")
    
        
    
                        
        