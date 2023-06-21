def solution(nums):
    n = len(nums)
    numset = set(nums)
    print(n, numset)
    
    if len(numset) < n/2:
        answer = len(numset)
    else:
        answer = n/2
    
    return answer