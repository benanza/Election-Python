# Election Results with Python

## Python script for counting poll results and returning winners/losers/vote counts from CSV

The situation: a small, rural town is modernizing its vote-counting process.

The poll data is inside the given csv file (election_data.csv), composed of three columns: Voter ID, County, and Candidate. The created Python script analyzes the votes and calculates each of the following:

The total number of votes cast, a complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won, and the winner of the election based on popular vote.

The script also prints the analysis to the terminal and exports a text file with the results appearing as follows:

```python
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
```
