def reverseString(given_string):

	for x in range(len(given_string)//2):
		temp = given_string[x]
		given_string[x] = given_string[len(given_string)-x-1]
		given_string[len(given_string)-x-1] = temp

	return given_string


print(reverseString(['a','b','c','d']))