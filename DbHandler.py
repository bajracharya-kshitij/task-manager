import mysql.connector as mc
from mysql.connector import errorcode

def save(task):
	print("Saving task...")
	
	connection = getDatabaseConnection()
	cursor = connection.cursor()
	
	createTable(cursor)
	insertData(cursor, task)

	connection.commit()

	cursor.close()
	connection.close()

	print("...Task saved")

def getDatabaseConnection():
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
	return connection

def createTable(cursor):
	print("Setting up table...")
	
	sql_command = """
		CREATE TABLE IF NOT EXISTS task (
			id INTEGER PRIMARY KEY,
			title VARCHAR(20),
			description VARCHAR(20)
		);
	"""

	cursor.execute(sql_command)
	print("...Table ready")

def insertData(cursor, task):
	numberOfEntries = getNumberOfEntries(cursor,task)
	sql_command = """
		INSERT INTO task (id, title, description) 
		VALUES ({id}, '{title}', '{description}');
	"""
	formatted_sql_command = sql_command.format(id=numberOfEntries+1, title=task.title, description=task.description)

	print("Executing command...")
	print(formatted_sql_command)

	cursor.execute(formatted_sql_command)

def getNumberOfEntries(cursor,task):
	sql_command = """
		SELECT COUNT(*) FROM task;
	"""
	cursor.execute(sql_command)
	return cursor.fetchone()[0]

	

	