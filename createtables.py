import mysql.connector

try:
	connection = mysql.connector.connect(host="localhost", 
		database = "test", 
		user = 'root', 
		password = 'Vignesh143')
	cursor = connection.cursor();
except mysql.connection.Error as error:
	print("Failed to execute the query: ", error);
finally:
	if (connection.is_connected()):
		cursor.close();
		connection.close();
		print("MySQL connection is closed")
