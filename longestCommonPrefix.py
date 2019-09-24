
def testFirstUnique(s):

	our_dict = {}
	s_l = len(s)

	for x in range(s_l):
		if s[x] in our_dict:
			our_dict.pop(s[x])
		else:
			our_dict[s[x]] = x

	for element in our_dict:
		print(our_dict[element])


testFirstUnique("aabbc")