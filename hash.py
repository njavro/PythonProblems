#IsUnique

def isUnique(given_string):

	if len(given_string) < 2:
		return False

	sorted_string = sorted(given_string)

	start_index = 0
	for i in range(len(sorted_string)):
		if sorted_string[i] != ' ':
			start_index = i
			break

	sorted_string = ''.join(sorted_string[start_index:])

	for c in range(1,len(sorted_string)):
		if sorted_string[c] == sorted_string[c-1]:
			return False

	return True



print(isUnique("moja baka voli puru"))
print(isUnique("abcdefghijklmn"))
print(isUnique(""))
print(isUnique("a"))
print(isUnique("aa"))
print(isUnique("bc"))
print(isUnique("abcdefgha"))