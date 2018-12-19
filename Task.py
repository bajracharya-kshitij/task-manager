class Task:
	def __init__(self, title, description):
		self.title = title
		self.description = description

	def showTask(self):
		print("Task details: ")
		print("Title: ", self.title)
		print("Description: ", self.description)

