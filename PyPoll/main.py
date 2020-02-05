# import appropriate modules for working with csv files across various operating systems
import csv
import os

# designate location of csv file we will be accessing
# (it's in the same directory as this python file)
csvpath = os.path.join("election_data.csv")

# open the csv using more efficient csv module language
with open(csvpath, newline = "") as csvfile:
    data_set = csv.reader(csvfile, delimiter=",")

    ## Used the following line to check the header contents, if any:
    #   print(next(data_set))
    ## yields: ['Voter ID', 'County', 'Candidate']

    # initialize counter at -1 in order to negate the header when counting rows/votes
    total_votes_count = -1

    # initialize counters for each candidate
    Khan_Count = 0
    Correy_Count = 0
    Li_Count = 0
    Otooley_Count = 0
    
    # initialize percentages for each candidate's vote count
    Khan_Percent = 0
    Correy_Percent = 0
    Li_Percent = 0
    Otooley_Percent = 0

    # loop through each row of the data set
    for row in data_set:

        # have a running counter that will yield the total number of rows
        # to use for calculating percentage of votes
        total_votes_count += 1

        # set up conditionals to identify contents of each 3rd column
        # and add to a counter that adds up all the votes for each candidate
        if row[2] == "Khan":
            Khan_Count += 1
        elif row[2] == "Correy":
            Correy_Count += 1
        elif row[2] == "Li":
            Li_Count += 1
        elif row[2] == "O'Tooley":
            Otooley_Count += 1
    
    # create a dictionary with that assigns each key (candidate)
    # with the amount of votes they collec
    Results = {"Khan":Khan_Count, "Correy":Correy_Count, "Li":Li_Count, "O'Tooley":Otooley_Count}
    
    # Calculate percentages and round to 3 decimal places
    Khan_Percent = round((Khan_Count / total_votes_count) * 100, 3)
    Correy_Percent = round((Correy_Count / total_votes_count) * 100, 3)
    Li_Percent = round((Li_Count / total_votes_count) * 100, 3)
    Otooley_Percent = round((Otooley_Count / total_votes_count) * 100, 3)
    
    # Find the max value from the values in the dictionary and return its key, then store as 'Winner'
    Winner = max(Results, key=Results.get)

    # create formatted text to print
    # (triple quotes allow multiple lines to be stored in string value)
    toprint = f"""Election Results
-----------------------
Total Votes: {total_votes_count} 
-----------------------
Khan: {Khan_Percent}% ({Khan_Count})
Correy: {Correy_Percent}% ({Correy_Count})
Li: {Li_Percent}% ({Li_Count})
O\'Tooley: {Otooley_Percent}% ({Otooley_Count})
-----------------------
Winner: {Winner} 
-----------------------"""

# print to Terminal
print(toprint)

# create txt file, print to it, and close
file = open("PyPoll.txt", "w")
file.write(toprint)
file.close()