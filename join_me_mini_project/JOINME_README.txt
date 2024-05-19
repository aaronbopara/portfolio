
JoinMe is a database used by a dating/social app. It contains two main tables: profile, holds the name 
and details of each user; seeking, has a row for the desired search criteria for each user. Individual 
users are identified by a profilename. 

There are four criteria columns in the seeking table:  

seeking_gender The gender to match to 
maxdistance The maximum distance (in kilometres) within which to find a match 
minage The minimum age to match to 
maxage The maximum age to match to

Each match must satisfy the seeking criteria for both parties. The suggested way to complete the 
match is to do it using joins in two stages. Take the matching criteria for each person (A) and the 
matching criteria for each person again (B) and then join the two sets of data where a person’s profile 
matches the criteria.

The relevant tables are located in the repository files as .csv files


