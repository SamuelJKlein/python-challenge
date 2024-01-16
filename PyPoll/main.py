import csv
import os

csv_path = os.path.join("Resources","election_data.csv")

#Dictionary to store canidates' names and vote counts
canidates = {}

#Variable to count total votes
vote_counter = 0

with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    header = next(csv_reader)
    #looping through all votes 
    for row in csv_reader:
        vote_counter += 1
        
        #if the canidate is already in the dictionary, add one to the vote count. 
        #else add the canidate and set equal to one. 
        if row[2] in canidates:
            canidates[row[2]][0] += 1
        else:
            #Canidate name is the key, and the value is a list where the first value is the canidates vote count. 
            #The second value will be the percentage of the total vote count
            canidates[row[2]] = [1,0]
            



#setting the second value in each canidates' list to the percentage of total votes
for key, value in canidates.items():
    value[1] = round(value[0] / vote_counter * 100, 3)
    
 




results = ["\nElection Results: \n\n","-------------------------\n\n","Total Votes: ",str(vote_counter),"\n\n-------------------------\n\n"]

#looping through the canidate results and adding them to the results array
for key, value in canidates.items():
    canidate_results = f"{key}: {value[1]}% ({value[0]})\n\n"
    results.append(canidate_results)






#finding and displaying the winner
winner = max(canidates, key=canidates.get)
results.append(f"-------------------------\n\nWinner: {winner}\n\n-------------------------")


print("".join(results))

# writing text file
txt_path = os.path.join("analysis","results.txt")
with open(txt_path, "w") as f:
        f.writelines(results)
