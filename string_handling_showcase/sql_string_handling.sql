/* Here are a selection of exercises which I completed to display string handling and cleaning 

The examples respective .csv files are located in the repositories files
*/ 

/* RAW JACK JILL */ 
WITH findpos AS
(
SELECT 
[str]
,CHARINDEX(' ',[str]) spacepos
,CHARINDEX('~',[str]) tildapos
,CHARINDEX('?',[str]) quespos
,CHARINDEX('/',[str]) slashpos
,CHARINDEX('!',[str]) exclpos
,CHARINDEX('$',[str]) dollarpos
FROM rawjackJill
)
SELECT 
[str]
,SUBSTRING([str],1,spacepos-1) [Jack]
,SUBSTRING([str],spacepos+1,tildapos-spacepos-1) [and]
,SUBSTRING([str],tildapos+1,quespos-tildapos-1) [Jill]
,SUBSTRING([str],quespos+1,slashpos-quespos-1) [went]
,SUBSTRING([str],slashpos+1,exclpos-slashpos-1) [up]
,SUBSTRING([str],exclpos+1,dollarpos-exclpos-1) [the]
,SUBSTRING([str],dollarpos+1,999999) [hill]
FROM findpos




/*RAWDOGS*/

WITH pos
AS
(
SELECT 
txt
,CHARINDEX('?',txt) AS qpos
,CHARINDEX(':',txt) AS colonpos
,CHARINDEX('@',txt) AS atpos
,CHARINDEX('-',txt) AS dash1
,CHARINDEX('-',txt,CHARINDEX('-',txt)+1) AS dash2		-- CHARINDEX(substring, string, start)
,CHARINDEX('?',txt,CHARINDEX('?',txt)+1)   AS qpos2     -- tries to find another one after the initial one
FROM [dbo].[rawdogs]
)
select txt
,LEFT(txt,qpos-1) Breed
,SUBSTRING(txt,qpos+1,colonpos-qpos-1) colour
,CASE
      WHEN dash2 > 0 THEN SUBSTRING(txt,colonpos+1,dash2-colonpos-1) 
      ELSE                SUBSTRING(txt,colonpos+1,dash1-colonpos-1) 
 END  age
,CASE 
      WHEN dash2 > 0 AND atpos > 0 THEN SUBSTRING(txt,dash2+1,atpos-dash2-1) 
      WHEN dash2 > 0 AND qpos2 > 0 THEN SUBSTRING(txt,dash2+1,qpos2-dash2-1) 
      WHEN dash2 = 0 AND qpos2 > 0 THEN SUBSTRING(txt,dash1+1,qpos2-dash1-1) 
      WHEN dash2 = 0 AND atpos > 0 THEN SUBSTRING(txt,dash1+1,atpos-dash1-1) 
 END  AS gender
,CASE 
      WHEN atpos > 0 THEN SUBSTRING(txt,atpos+1,999) 
	  ELSE  SUBSTRING(txt,qpos2+1,999) 
 END  AS name
from pos
;


