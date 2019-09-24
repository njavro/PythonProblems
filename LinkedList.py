class Node(object):
	"""docstring for Node"""
	def __init__(self, value = None):
		self.value = value
		self.next = None


class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = Node()
		self.tail = Node()
		self.size = 0

	def addNode(self,value):
		previous_node = self.head
		while previous_node.next != None:
			previous_node = previous_node.next

		new_node = Node(value)
		previous_node.next = new_node
		self.tail.next = new_node
		self.size += 1

	def printList(self):
		current_node = self.head
		output_list = []
		while current_node.next != None:
			output_list.append(current_node.next.value)
			current_node = current_node.next
		print(output_list)

	def addAtBeginning(self, value):
		previous_node = self.head
		new_node = Node(value)
		new_node.next = previous_node.next
		previous_node.next = new_node

	def addAtEnd(self,value):
		new_node = Node(value)
		self.tail.next.next = new_node
		self.tail.next = new_node


	def reverse(self):
		#Something is wrong is adjust to self.head = Node()
		if self.head == None:
			return self.head
		elif self.head.next == None:
			return self.head

		original_head = self.head.next
		cur_head = self.head.next

		while original_head.next:
			p = original_head.next
			original_head.next = p.next
			p.next = cur_head
			cur_head = p

		#self head should be one before P
		new_head = Node()
		new_head.next = p
		self.head = new_head



	def removeElement(self,value):

		fast = self.head
		slow = self.head

		if slow.next == fast.next == None:
			return
		elif slow.next.next == fast.next.next == None:
			return

		while fast:
			while fast.next is not None and fast.next.value != value:
				fast = fast.next
				slow = slow.next

			fast = fast.next
			while fast is not None and fast.value == value:
				fast = fast.next

			slow.next = fast
			slow = fast


	def checkPalindrome(self):

		if self.size == 0:
			return
		elif self.size == 1:
			return

		if self.size%2 == 0:
			fake_head = Node()
			fake_head.next = self.head.next
			curr = self.head.next
			for x in range(self.size//2):
				self.head = self.head.next

			self.reverse()






		






'''	def removeNode(self,index):
		if index >= self.size:
			print("OUT OF BOUNDS")
			return

		counter = 0
		previous_node = self.head
		while True:
			if counter == index:
				previous_node.next = previous_node.next.next
				self.size -= 1
			else:
				previous_node = previous_node.next
				counter +=1
'''


		



def randomList(LinkedList , size , max_number):
	import random
	for x in range(size):
		LinkedList.addNode(random.randint(0,max_number))







my_list = LinkedList()

my_list.addNode(1)
my_list.addNode(2)
my_list.addNode(3)
my_list.addNode(3)
my_list.addNode(2)
my_list.addNode(1)

my_list.checkPalindrome()
my_list.printList()

#my_list.printList()

		

