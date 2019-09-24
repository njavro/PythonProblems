#Given 2 strings check if one is permutaion of other

def isPermutation(string1, string2):

	#Test edge cases
	if len(string1)!=len(string2):
		return False
	elif len(string1) == len(string2) == 0:
		return False



	dictionary_1 = {}
	dictionary_2 = {}

	#Fill dict1
	for character in string1:
		if character in dictionary_1:
			dictionary_1[character] += 1
		else:
			dictionary_1[character] = 1


	#Fill dict2
	for character in string2:
		if character in dictionary_2:
			dictionary_2[character] += 1
		else:
			dictionary_2[character] = 1


	#Go through dictionary 1 and check if each letter occurs same amount of times as in second dictionary
	for character in dictionary_1:
		if character not in dictionary_2:
			return False
		elif dictionary_2[character] != dictionary_1[character]:
			return False


	return True


print(isPermutation("abcdefgh", "abcdefgh"))
print(isPermutation("abcdefgh", "fghcbdae"))
print(isPermutation("a", "a"))
print(isPermutation("a", "aaaaa"))
print(isPermutation("abc", "abcd"))
print(isPermutation("a", "a"))
print(isPermutation("", "abcdefgh"))
print(isPermutation("", ""))