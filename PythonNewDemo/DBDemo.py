import pyodbc

# Open database connection
db = pyodbc.connect("DRIVER={SQL Server};SERVER=.\Admin;DATABASE=Test;UID=sa;PWD=sa@123")



# disconnect from server
db.close()