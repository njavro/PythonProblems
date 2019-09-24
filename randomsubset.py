import random

def computeRandomSet(n ,k):
	#Compute subset of given_set of size k

	counter = 0
	subset = set()
	

	while counter < k:

		random_num = random.randint(0,n)
		print("Current random num is: ", random_num)

		if random_num not in subset:
			print("This number is added to set: ", random_num)
			subset.add(random_num)
			counter += 1
			
		print("Subset currently is: ", subset)

	return subset




print( computeRandomSet(10,10) )

		