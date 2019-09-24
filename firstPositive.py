def solution(A):
    # write your code in Python 3.6
    our_dict = {}
    
    for number in A:
        if number in our_dict:
            our_dict[number] += 1
        else:
            our_dict[number] = 1
    
    
    for x in range(1,max(A)+1):
        if x not in our_dict:
            return x
    return max(A)+1
print(solution([1,2,3]))



