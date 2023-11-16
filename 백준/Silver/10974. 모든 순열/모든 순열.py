N = int(input())

nums = [(i) for i in range(N+1)]

def dfs(n):     
    visited.append(n)
       
    if(len(visited)) == N:
        print(* visited)
        return

    for k in range(1,N+1):
        if k not in visited:
            dfs(k)
            visited.pop()
            
for i in range(N):
    visited = []
    dfs(i+1)
# visited=[]
# dfs(1)