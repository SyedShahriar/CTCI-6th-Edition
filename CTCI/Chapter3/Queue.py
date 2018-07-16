class Queue():

	def __init__(self):
		self.array = []

	def enqueue(self,item):
		self.array.append(item)

	def dequeue(self):
		if self.array:
			return self.array.pop(0)
		else: return None

if __name__ == '__main__':
	test = Queue()
	test.enqueue(10)
	test.enqueue(15)

	print test.dequeue()
