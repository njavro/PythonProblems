class Node(object):
	"""docstring for Node"""
	def __init__(self, value = None):
		
		self.value = value
		self.left = None
		self.right = None


class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, root):
		self.root = Node(root)
		


	def preOrder(self, root, given_list):

		if root:
			given_list.append(root.value)
			self.preOrder(root.left,given_list)
			self.preOrder(root.right,given_list)

		return given_list



	def inOrder(self, root, given_list):

		if root:
			self.inOrder(root.left,given_list)
			given_list.append(root.value)
			self.inOrder(root.right,given_list)

		return given_list


	def postOrder(self, root, given_list):

		if root:
			self.postOrder(root.left,given_list)
			self.postOrder(root.right,given_list)
			given_list.append(root.value)

		return given_list


	def traverseTree(self, traverseType):

		my_l = []

		if traverseType.upper() == "INORDER":
			print(self.inOrder(self.root,my_l))
			my_l.clear()
			return
		elif traverseType.upper() == "POSTORDER":
			print(self.postOrder(self.root,my_l))
			my_l.clear()
			return
		elif traverseType.upper() == "PREORDER":
			print(self.preOrder(self.root,my_l))
			my_l.clear()
			return
		else:
			print("NO SUCH TRAVERSE EXISTS!")
			return


	def iterativePreOrder(self):
		our_stack = []
		ret_l = []
		if self.root:
			our_stack.append(self.root)

		while len(our_stack) > 0:
			popped_item = our_stack.pop()
			ret_l.append(popped_item.value)
			if(popped_item.right):
				our_stack.append(popped_item.right)

			if(popped_item.left):
				our_stack.append(popped_item.left)
		return ret_l


	def depth(self):
		return self.maxDepth(root = self.root)


	def maxDepth(self, root):
		if root == None:
			return 0

		depth = 0
		if root:
			depth+=1
			left_depth = self.maxDepth(root.left)
			right_depth = self.maxDepth(root.right)
			if left_depth > right_depth:
				depth += left_depth
			else:
				depth += right_depth
		return depth







tree = BinaryTree(9)
tree.root.left = Node(10)
tree.root.right = Node(60)

tree.root.left.left = Node(99)
tree.root.left.right = Node(4)

tree.root.right.left = Node(69)
tree.root.right.right = Node(70)


print ( tree.iterativePreOrder() )
print(tree.traverseTree("preorder"))


print(tree.depth())




		
		