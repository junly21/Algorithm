def solution(clothes):
    answer = 0
    count = 1
    dictionary = {}
    for cloth in clothes:
        if cloth[1] not in dictionary:
            dictionary[cloth[1]] = 1
        elif cloth[1] in dictionary:
            dictionary[cloth[1]] += 1
    
    print(dictionary)
    
    combi_nums = dictionary.values()
    
    
    for i in combi_nums:
        count = count*(i+1)

    count = count - 1
    
    return count
