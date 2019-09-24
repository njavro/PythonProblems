def oneAway(string1, string2):

	count_edits = 0

	count_edits += abs(len(string1) - len(string2))

	if len(string1) < len(string2):
		shorter_string = string1
		longer_string = string2
	else:
		shorter_string = string2
		longer_string = string1

	for x in range(len(shorter_string)):
		if shorter_string[x] != longer_string[x]:
			count_edits += 1

	if count_edits > 1:
		return False
	else:
		return True