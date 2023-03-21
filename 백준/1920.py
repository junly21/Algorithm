N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
Nlist.sort()
def binary_search(target):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if Nlist[mid] == target:
            return 1
        elif Nlist[mid] > target:
            end = mid -1
        else: #Nlist[mid] <target
            start = mid + 1
    return 0
    
for i in range(0,M):
    print(binary_search(Mlist[i]))