def solution(array, commands):
    answer = []
    for command in commands:
        start = int(command[0])
        end = int(command[1])
        temp_list = array[start-1:end]
        temp_list.sort()
        target = int(command[2])
        answer.append(temp_list[target-1])
    return answer