import mysql.connector
from mysql.connector import errorcode

class Task:
	def __init__(self, title, description):
		self.title = title
		self.description = description

	def showTask(self):
		print("Task details: ")
		print("Title: ", self.title)
		print("Description: ", self.description)

def handleDatabaseConnection():
		try:
			connection = mysql.connector.connect (
				user = 'root',
				password = 'root',
				host = 'localhost',
				database = 'taskmanager'
			)
			print("Database connected!")
		except mysql.connector.Error as e:
			if (e.errno == errorcode.ER_ACCESS_DENIED_ERROR):
				print("Wrong user and/or password")
			elif (e.errno == errorcode.ER_BAD_DB_ERROR):
				print("Database doesn't exist")
			else:
				print(e)

if __name__ == '__main__':
	handleDatabaseConnection()
	name = input("Enter task name: ")
	description = input("Provide a description: ")

	task = Task(name, description)
	task.showTask()

