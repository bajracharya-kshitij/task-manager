import DbHandler
import Task

if __name__ == '__main__':
	DbHandler.handleDatabaseConnection()
	name = input("Enter task name: ")
	description = input("Provide a description: ")

	task = Task.Task(name, description)
	task.showTask()