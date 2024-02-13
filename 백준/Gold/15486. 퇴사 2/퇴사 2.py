import sys
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dptable = [0 for i in range(1500001)] 
temp = 0
for i in range(n-1,-1,-1):
    if board[i][0] + i <= n:
        day = board[i][0]
        dptable[i] = max(dptable[i+1], board[i][1] + dptable[i+day])
    else:
        dptable[i] = dptable[i+1]
print(dptable[0])