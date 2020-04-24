import mysql.connector

try:
	connection = mysql.connector.connect(
		host="localhost", 
		username="root", 
		password="Vignesh143",
		database="test")
	print("User " + connection.user 
		+ " Successfully connected to the database: " 
		+ connection.database)
except mysql.connection.Error as error:
	print("Failed to execute the query: ", error);
finally:
	if (connection.is_connected()):
		connection.close();
	print("MySQL connection is closed")
	