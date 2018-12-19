import DbHandler
import Task

if __name__ == '__main__':
	while True:
		name = input("Enter task name: ")
		description = input("Provide a description: ")

		task = Task.Task(name, description)
		task.showTask()
		DbHandler.save(task)

		decision = input("Add another task? (Enter y for Yes or any other key to quit)")
		if(decision.lower() != 'y'):
			break