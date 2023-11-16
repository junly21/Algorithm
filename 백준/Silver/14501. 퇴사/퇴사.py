#입력이 15일이네?
#가능한 모든 경우를 탐색 해볼만 한데?
#왜냐면 하냐or안하냐니까 최대 2^15의 가짓수임 모든 조합이
# 일단 N일 채우면 종료
# 1일차 에서부터 상담을 선택 하냐 안하냐로 분기 
import sys
N = int(input())
T=[0]
P=[0]
for i in range(N):
  t, p = map(int,sys.stdin.readline().split())
  T.append(t)
  P.append(p)

# print(T)
# print(P)

sum_list = []

def dfs(n,sum):
  if n == N+1:
    sum_list.append(sum)
    return
  elif n>N+1:
    return

  dfs(n+T[n], sum + P[n])
  dfs(n+1, sum)

dfs(1,0)

print(max(sum_list))