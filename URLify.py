#URLify replace all places in string with %20
#You're given array and "true" length

def URLify(given_string,true_length):

	string_list = [None]*true_length

	for i in range(true_length):
		if given_string[i] != ' ':
			string_list[i] = given_string[i]
		else:
			string_list[i] = '%20'

	return ''.join(string_list)

print(URLify("abc cba",7))
print(URLify("Mr John Smith    ",13))
print(URLify(" abccba ",6))
print(URLify("       ",7))