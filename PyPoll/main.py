
import os
import csv
Path = os.path.join("Resources","election_data.csv")
with open(Path,mode='r',encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)
    count = 0
    votes = {}
    Count_of_votes = []
   
    List_of_Candidates = set() #Created a set which will store the names of candidates because sets doesnt store duplicate values
    for row in csvreader:
        count = count + 1      #Total no. of votes
        List_of_Candidates.add(row[2])  #Stores Unique values
        if row[2] in votes:
            votes[row[2]] = votes[row[2]] + 1
        else:
            votes[row[2]] = 1                 #Creates a Dictionary votes and maps unique candidates to the no. of votes
    print("Election Results:")
    print("---------------------------------")
    print(f"The total number of votes  are:{count}")
    print("---------------------------------")
   
    Max_Value = max(votes.values())       #Calculates the max. of values in votes
    for key,values in votes.items():
        if values == Max_Value:
            print(f"Winner:{key}")       #Finds out key corresponding to max.value
            print("---------------------------------")
        percentage = round(((values/count)*100),2)    #calculates percentage of votes each candidate won
        print(f"{key}:{percentage}% ({values})")
outpath = os.path.join("Analysis","Output.txt")        #Exporting the output in a text file
with open(outpath,mode='w',encoding='utf8') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter = ',')

    print("Election Results:",file = csvfile)
    print("---------------------------------",file=csvfile)
    print(f"The total number of votes  are:{count}",file=csvfile)
    print("---------------------------------",file=csvfile)
    values = len(votes.values())
    Max_Value = max(votes.values())
    for key,values in votes.items():
        if values == Max_Value:
            print(f"Winner:{key}",file=csvfile)
            print("---------------------------------",file=csvfile)
        percentage = round(((values/count)*100),2)
        print(f"{key}:{percentage}% ({values})",file=csvfile)

