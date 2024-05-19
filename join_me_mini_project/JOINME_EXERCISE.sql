/* 
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

The examples respective .csv files are located in the repositories files

*/ 

USE joinme;

/*1. This query displays a table which matches each profiles with profiles detailed in their seeking preferences.
*/

with pro as
(
SELECT p1.profilename, p1.firstname, p1.lastname
		, DATEDIFF(YEAR,p1.birthdate, GETDATE()) AS age
		, p1.gender, p1.location
		, s1.maxdistance, s1.seeking_gender, s1.minage, s1.maxage
		FROM profile AS p1
		JOIN seeking AS s1 ON p1.profilename = s1.profilename
		)
SELECT p.profilename, p.firstname, p.lastname, p.age, p.gender
	, ROUND(dbo.distancem(p.location,q.location)/1000,0) AS distance
	, q.profilename, q.firstname, q.lastname, q.age, q.gender
FROM pro AS p
JOIN pro AS q
ON p.age BETWEEN q.minage AND q.maxage
AND q.age BETWEEN p.minage AND p.maxage
AND dbo.distancem(p.location, q.location)/1000 <=p.maxdistance
AND dbo.distancem(p.location, q.location)/1000 <=q.maxdistance
AND p.gender = q.seeking_gender
AND q.gender = p.seeking_gender
AND p.profilename != q.profilename
ORDER BY p.profilename;

/* 2. This query calculates the average distance to a match for each profile : 8.7KM */

with pro as
(
SELECT p1.profilename, p1.firstname, p1.lastname
		, DATEDIFF(YEAR,p1.birthdate, GETDATE()) AS age
		, p1.gender, p1.location
		, s1.maxdistance, s1.seeking_gender, s1.minage, s1.maxage
		FROM profile AS p1
		JOIN seeking AS s1 ON p1.profilename = s1.profilename
		)
SELECT AVG(dbo.distancem(p.location,q.location)/1000.0) AS avg_distance
FROM pro p
JOIN pro q
ON p.age BETWEEN q.minage AND q.maxage
AND q.age BETWEEN p.minage AND p.maxage
AND dbo.distancem(p.location, q.location)/1000 <=p.maxdistance
AND dbo.distancem(p.location, q.location)/1000 <=q.maxdistance
AND p.gender = q.seeking_gender
AND q.gender = p.seeking_gender
AND p.profilename != q.profilename;

/* This query displays the profiles which are non-matches to a profile : */

with pro as
(
SELECT p1.profilename, p1.firstname, p1.lastname
		, DATEDIFF(YEAR,p1.birthdate, GETDATE()) AS age
		, p1.gender, p1.location
		, s1.maxdistance, s1.seeking_gender, s1.minage, s1.maxage
		FROM profile AS p1
		JOIN seeking AS s1 ON p1.profilename = s1.profilename
		)
SELECT COUNT(DISTINCT p.profilename) AS no_matches
FROM pro p
LEFT OUTER JOIN pro q
ON p.age BETWEEN q.minage AND q.maxage
AND q.age BETWEEN p.minage AND p.maxage
AND dbo.distancem(p.location, q.location)/1000 <=p.maxdistance
AND dbo.distancem(p.location, q.location)/1000 <=q.maxdistance
AND p.gender = q.seeking_gender
AND q.gender = p.seeking_gender
AND p.profilename != q.profilename
WHERE q.profilename IS NULL;

