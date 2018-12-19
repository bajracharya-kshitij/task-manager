import mysql.connector as mc
from mysql.connector import errorcode

def handleDatabaseConnection():
	print("Trying to connect to the database...")
	try:
		connection = mc.connect (
			user = 'root',
			password = 'root',
			host = 'localhost',
			database = 'taskmanager'
		)
		print("Database connected!")
	except mc.Error as e:
		if (e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
			print("Wrong user and/or password")
		elif (e.errno == errorcode.ER_BAD_DB_ERROR):
			print("Database doesn't exist")
		else:
			print(e)

	cursor = connection.cursor()

	cursor.execute("DROP TABLE IF EXISTS task")

	sql_command = """
		CREATE TABLE task (
			id INTEGER PRIMARY KEY,
			title VARCHAR(20),
			description VARCHAR(20)
		);
	"""

	cursor.execute(sql_command)

	connection.commit()

	cursor.close()
	connection.close()