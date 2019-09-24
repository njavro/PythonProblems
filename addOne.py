
def addOne(digits):

	carry = 0

	if len(digits) == 1 and digits[0] == 9:
		return [1,0]

	for i in range(len(digits)-1,-1,-1):

		#Special case when greatest digit is 9 means we have to make new larger list
		if(i==0 and digits[i] + carry > 9):
			digits[i] = digits[i] + carry - 10
			carry=0
			new_list = []
			new_list.append(1)
			for number in digits:
				new_list.append(number)
			return new_list


		if (i==len(digits)-1):
			if (digits[i]+1>9):
				digits[i] = digits[i] + 1 - 10
				carry = 1
			else:
				digits[i] = digits[i] + 1
				carry = 0
		else:
			if(digits[i]+carry>9):
				digits[i] = digits[i] + carry - 10
				carry = 1
			else:
				digits[i] = digits[i] + carry
				carry = 0


	return digits


print(addOne([9,8,9,9]))