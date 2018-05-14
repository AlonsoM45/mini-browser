DECLARE @json VARCHAR(MAX)
SELECT @json = BulkColumn
FROM OPENROWSET (BULK 'C:\Users\Casa\Desktop\mini-browser-master\100.json', SINGLE_CLOB) as j

SELECT *
FROM OPENJSON(@json)
WITH (   
	Name    varchar(100) '$.reviewerName' ,  
	Summary varchar(400)     '$.summary'
 ) 

SELECT @json