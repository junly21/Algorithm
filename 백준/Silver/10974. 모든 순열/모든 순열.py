N = int(input())

nums = [(i) for i in range(N+1)]

def dfs(n, depth):     
    visited.append(n)
    
    if(depth) == N:
        print(* visited)
        return

    for num in range(1,N+1):
        if num not in visited:
            dfs(num, depth+1)
            visited.pop()
            
for i in range(N):
    visited = []
    dfs(i+1, 1)
# visited=[]
# dfs(1)