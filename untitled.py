
def isUnique(given_string):

    if len(given_string)==0:
        return False
    elif len(given_string)==1:
        return True

    #BottleNeck O(NlogN)
    sorted_string = sorted(given_string)

    for i in range(1,len(sorted_string)):
        if sorted_string[i] == sorted_string[i-1]:
            return False
    return True



my_string = "abcdefghijla"

print(isUnique(my_string))