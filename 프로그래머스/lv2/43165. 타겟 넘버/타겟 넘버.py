def dfs(step,numbers,target,total):
    #종료조건
    if step == len(numbers):
        if target == total:
            return 1
        else:
            return 0
    return dfs(step+1, numbers, target, total+numbers[step]) + dfs(step+1, numbers, target, total-numbers[step])
    
def solution(numbers, target):
    answer = 0
    
    answer = dfs(0,numbers,target,0)
    return answer