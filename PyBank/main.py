import os 
import csv
import math
path = os.path.join("Resources","budget_data.csv")
count = 0
total = 0
value = []
months = []
Dict= {}
with open(path,mode = 'r',encoding = 'utf8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)
    previousRow = 0
    for row in csvreader:
        count = count + 1                          #counting total no. of rows here
        total = float(total) + float(row[1])       #total amount
        difference = float(row[1]) - previousRow   #calculating change in profit/loss 
        previousRow = float(row[1])                #storing value of previous cell
        if count > 1:
            Dict[row[0]]= difference            #Creating a dictionary for storing the values as Months:Difference pair 
    print("Financial Analysis")
    print("--------------------------")
    max_change = max(Dict.values())            #calculating maximum change
    min_change = min(Dict.values())            #calculating minimum change
    
    average = sum(Dict.values())/len(Dict.values())
       
    print(f"The total no. of months included in the data set are:{count}")
    print(f"The net total amount of Profit/Losses over the entire period is : {total}")
    print(f"The average of the changes in Profit/Losses over the entire period is: {average}")
    
    for key,values in Dict.items():           #Method to find out key,value values
        if values == max_change:
            print(f"Greatest Increase in Profits:{key} (${values})")
        
        if values == min_change:
            print(f"Greatest Decrease in Profits:{key} (${values})")
       
    

outpath = os.path.join("Analysis","output.txt")
with open(outpath,mode='w',encoding='utf8') as csvfile: #Exporting the output in a text file
    csvwriter = csv.writer(csvfile,delimiter = ',')
    
    max_change = max(Dict.values()) 
    min_change = min(Dict.values()) 
    
    average = sum(Dict.values())/len(Dict.values())
    print("Financial Analysis",file=csvfile)
    print("--------------------------",file=csvfile)   
    print(f"The total no. of months included in the data set are:{count}",file= csvfile)
    print(f"The net total amount of Profit/Losses over the entire period is : {total}",file= csvfile)
    print(f"The average of the changes in Profit/Losses over the entire period is: {average}",file= csvfile)
    
    for key,values in Dict.items(): 
        if values == max_change:
            print(f"Greatest Increase in Profits:{key} (${values})",file= csvfile)
        
        if values == min_change:
            print(f"Greatest Decrease in Profits:{key} (${values})" ,file= csvfile)
       
           
        #References:https://stackoverflow.com/questions/45461406/python-output-to-a-text-file
        #https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary