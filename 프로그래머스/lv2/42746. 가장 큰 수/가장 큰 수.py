# def solution(numbers):
#     answer = []
#     num_list = []
#     numbers.sort(reverse=True)
#     numbers=str(numbers)
    
#     print(numbers)
#     num_list = sorted(numbers, key=lambda x:x)
#     # print(num_list)
    
#     print(num_list)
#     return answer

from itertools import permutations
def solution(numbers):
    num_length = len(numbers)
    numbers = list(map(str, numbers))
    
    #result = max(set(("".join(x)) for x in list(permutations(numbers, num_length))))
    result = max(("".join(x)) for x in list(permutations(numbers, num_length)))

    return result 