n,m,v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    matrix[start][end] = 1
    matrix[end][start] = 1

stack = []
stack.append(v)
# visited = [False] * (n+1)
visited = []

def dfs(current):
    # while stack:
    #     current = stack.pop()
    #     if visited[current] == False:
    #         print(current, end=' ')
    #     if visited[current] == False:
    #         visited[current] = True
    #         for i in range(1, n+1):
    #             if matrix[current][i] == 1 and visited[i] == False:
    #                 stack.append(i)
    if current not in visited:
        visited.append(current)
        for i in range(1, n+1):
            if matrix[current][i] == 1 and i not in visited:
                dfs(i)
        

dfs(v)

print(*visited)
from collections import deque
queue = deque()
queue.append(v)
visited = [False] * (n+1)
def bfs():
    while queue:
        current = queue.popleft()
        if visited[current] == False:
            print(current, end=' ')
        if visited[current] == False:
            visited[current] = True
            for i in range(1, n+1):
                if matrix[current][i] == 1 and visited[i] == False:
                    queue.append(i)

bfs()