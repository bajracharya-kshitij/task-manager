class Task:
	def __init__(self, title, description):
		self.title = title
		self.description = description

	def showTask(self):
		print("Task details: ")
		print("Title: ", self.title)
		print("Description: ", self.description)

if __name__ == '__main__':
	name = input("Enter task name: ")
	description = input("Provide a description: ")

	task = Task(name, description)
	task.showTask()

