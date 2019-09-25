class TrieNode(object):
	"""docstring for TrieNode"""
	def __init__(self, character):
		self.character = character

		self.children = []

		self.isWord = False

		self.maxval = 0


#Add word

def add(root,word):
	"""
	Add a word to trie
	"""
	node = root

	for character in word:

		found = False

		#Search character in list of children
		for child in node.children:

			if child.character == character:
				#Character found!
				node = child
				found = True
				break

		if not found:
			new_node = TrieNode(character)
			node.children.append(new_node)
			node = new_node

	#Mark as end of word
	node.isWord = True


def prefixFind(root,prefix):

	node = root

	if not root.children:
		#Empty Trie
		return False

	for character in prefix:
		not_found = True

		for child in node.children:
			if child.character == character:
				not_found = False
				node = child
				break


		if not_found:
			#Iterated yet still did not find a character
			return False

	return True



root = TrieNode('*')
add(root, 'anton')
add(root,'kitchen')
add(root,'antonija')
add(root,'anemija')

print(prefixFind(root,'rant'))
print(prefixFind(root,'ant'))
print(prefixFind(root,'anton'))
print(prefixFind(root,'antologija'))
print(prefixFind(root,'catherine'))
print(prefixFind(root,'kit'))








		