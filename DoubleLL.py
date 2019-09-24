class Node(object):
	"""docstring for Node"""
	def __init__(self, value = None):
		
		self.value = value
		self.next = None
		self.previous = None



class DoublyLinkedList(object):
	"""docstring for DoublyLinkedList"""
	def __init__(self):
		self.head = Node()
		self.size = 0


	def get(self,index):

		if index < 0 or index >= self.size:
			return -1


		'''IMPLEMENT THIS SHIT LATER'''
		
		