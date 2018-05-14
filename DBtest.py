import pyodbc

cnxn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};"
                      "Server= (localdb)\MSSQLLocalDB;"
                      "Trusted_Connection=yes;")

print("ALLO")
cursor = cnxn.cursor()
cursor.execute('SELECT * FROM DBMiniBrowser.dbo.Review')
for row in cursor:
    print(row)
print("DONE")
