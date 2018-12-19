class Task:
	def __init__(self, title):
		self.title = title

	def showTask(self):
		print("The title for the task is", self.title)

if __name__ == '__main__':
	task = Task("Write First Program")
	task.showTask()