N = int(input())
cols = [0]*N
answer = 0
def deployee_queen(current_row):
    #종료조건
    global answer
    if current_row == N:
        answer+=1
        return

    for i in range(N):
        #예외처리
        cols[current_row] = i
        for prev_row in range(current_row):#이전단계들 순회하는데
            #cols[current_row] = i
            if cols[prev_row] == i: #이전 단계와 현재 colum겹치면 스킵
                break
            if abs(cols[prev_row] - i) == current_row-prev_row: #이전단계와 현재가 대각선이면 스킵
                break
        else:
            # cols[current_row] = i
            deployee_queen(current_row+1)

deployee_queen(0)
print(answer)