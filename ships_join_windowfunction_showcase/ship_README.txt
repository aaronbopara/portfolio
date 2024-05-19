
This is a SQL Query which establishes the profit gained or lost from a series of ship voyages. 

Outgoings are calculated by multiplying ships.cost_per_mile by the distance travelled during each voyage. 
Voyage.voyage_number for each ship indicates the sequence of theship’s voyages. 
The ship’s first Voyage starts from the ship’s home port. 
Use the Routes table to calculate the distance from the port from which the ship leaves to the destination port.  
The Routes_bothways table holds the distances for the journey between the Ports both ways around. 
i.e. Routes_bothways holds a row for the journey and a second row for the reverse journey.  
There is a row for every port-to-port combination in Routes that exists in voyages

The CSV files are located in the repositories files

