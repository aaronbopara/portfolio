This is an example of a SQL procedure I made to calculate the wages of a single employee who's overtime data is stored in this table. 
The procedure accepts four paramters 


 The date range over which the calculation is to take place (@p_start_date and 
@p_end_date) 

 The standard number of hours each day (@p_standard_hrs) 

 The standard hourly rate (£) (@p_standard_wage)

The normal wage for a single day is calculated using @p_standard_wage*@p_stantard_hrs. 
 
However, If the Overtime table contains data for a date, then use the calculated figure from the 
overtime table (hours*@p_standard_wage*rate) instead of the @p_standard_wage 
*@p_standard_hours. There is no weekend working unless there is an entry in the overtime table 
for a weekend date.

The overtime.csv file is located in the repository files

