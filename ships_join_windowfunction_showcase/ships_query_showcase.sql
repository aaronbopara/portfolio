
/*
This is a SQL Query which establishes the profit gained or lost from a series of ship voyages. 

Outgoings are calculated by multiplying ships.cost_per_mile by the distance travelled during each voyage. 
Voyage.voyage_number for each ship indicates the sequence of theship’s voyages. 
The ship’s first Voyage starts from the ship’s home port. 
Use the Routes table to calculate the distance from the port from which the ship leaves to the destination port.  
The Routes_bothways table holds the distances for the journey between the Ports both ways around. 
i.e. Routes_bothways holds a row for the journey and a second row for the reverse journey.  
There is a row for every port-to-port combination in Routes that exists in voyages

The CSV files are located in the repositories files

*/


WITH voy AS
(SELECT 
 sh.ship_name
 ,sh.cost_per_mile
,v.voyage_number
,LAG(destination_port) OVER (partition by sh.ship_name order by v.voyage_number) lagport
,COALESCE(LAG(destination_port) OVER (partition by sh.ship_name order by v.voyage_number),sh.home_port) start_port
,destination_port
,v.voyage_earning
FROM ships sh
JOIN Voyage v
ON v.ship_name = sh.ship_name
)
SELECT 
 v.ship_name
,v.voyage_number
,v.lagport
,v.start_port
,v.destination_port
,v.voyage_earning
,(d.distance*v.cost_per_mile)  outgoing
,v.voyage_earning - (d.distance*v.cost_per_mile) profit
FROM voy v
JOIN  dbo.routes_bothways d
ON d.port1 = v.start_port
AND d.port2 = v.destination_port
ORDER BY ship_name
;

