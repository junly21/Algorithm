def solution(participant, completion):
    answer = {} #딕셔너리
    for i in participant:
        answer[i] = answer.get(i, 0) + 1 #answer에 추가 후 value 0에서 1로 변경
    for j in completion:
        answer[j] -= 1 #완주자 value를 다시 0으로 변경
    for k in answer:
        if answer[k] != 0:
            return k
