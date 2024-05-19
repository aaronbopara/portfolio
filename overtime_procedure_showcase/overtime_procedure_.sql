/* This is an example of a SQL procedure I made to calculate the wages of a single employee who's overtime data is stored in this table. 
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

*/ 

USE misc
CREATE OR ALTER PROCEDURE Calc_wages (@p_start_date DATE,@p_end_date DATE, @p_standard_wage DECIMAL(10,2),@p_standard_hrs DECIMAL(10,2))
AS
BEGIN

	DECLARE @v_day_total     DECIMAL(10,2) = 0; 
	DECLARE @v_total         DECIMAL(10,2) = 0; 

	WHILE @p_start_date <= @p_end_date
	BEGIN
	  IF DATENAME(weekday,@p_start_date) NOT IN ('Saturday','Sunday') OR  EXISTS (SELECT 'ThisdoesnotMatter' FROM misc.dbo.overtime where work_date = @p_start_date)
		  BEGIN 
			  SET @v_day_total = (SELECT hours*rate*@p_standard_wage 
								  FROM misc.dbo.overtime 
								  WHERE work_date = @p_start_date);
			  SET @v_total = @v_total+COALESCE(@v_day_total,@p_standard_hrs*@p_standard_wage);
		  END;

	  SET @p_start_date = DATEADD(day,1,@p_start_date);

	END;
	PRINT 'The total gross pay is : £'+CAST(@v_total AS VARCHAR(100));
END;
SELECT COALESCE(hours,8)*COALESCE(rate,1)*10
							  FROM misc.dbo.overtime 
							  WHERE work_date = '2022-jan-20'

-- Rate = £10 - Result should be £120
exec Calc_wages  @p_start_date  = '2022-JAN-01', @p_end_date = '2022-JAN-02', @p_standard_wage = 10,@p_standard_hrs = 8;

-- Rate = £20 - Result should be £240
exec Calc_wages  @p_start_date  = '2022-JAN-01', @p_end_date = '2022-JAN-02', @p_standard_wage = 20,@p_standard_hrs = 8;

-- Rate = £10 end_date = '2022-JAN-15'- Result should be £920
exec Calc_wages  @p_start_date  = '2022-JAN-01', @p_end_date = '2022-JAN-15', @p_standard_wage = 10,@p_standard_hrs = 8;

-- Rate = £10 end_date = '2022-JAN-15'- Result should be £1000
exec Calc_wages  @p_start_date  = '2022-JAN-01', @p_end_date = '2022-JAN-16', @p_standard_wage = 10,@p_standard_hrs = 8;

-- Rate = £10 end_date = '2022-JAN-17'- Result should be £1100
exec Calc_wages  @p_start_date  = '2022-JAN-01', @p_end_date = '2022-JAN-17', @p_standard_wage = 10,@p_standard_hrs = 8;


select 0+100

select *,datename(weekday,work_date)  FROM misc.dbo.overtime  

SELECT hours*rate*10
							  FROM misc.dbo.overtime
where work_date = '2022-jan-02'

select datename(weekday,'2022-jan-02')