#String compression

def compress(given_string):

	our_dict  = {}

	for character in given_string:
		if character in our_dict:
			our_dict[character] +=1
		else:
			our_dict[character] = 1

	new_string = []

	for character in our_dict:
		new_string.append(character)
		new_string.append(str(our_dict[character]))

	if len(''.join(new_string)) < len(given_string):
		return ''.join(new_string)
	else:
		return given_string


print( compress("aaabbc"))