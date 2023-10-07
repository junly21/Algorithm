N = int(input())
A = list(map(int, input().split()))
ans = 0
def isOdd(num):
    if (num%2 == 0):
        return False
    elif num%2 != 0:
        return True
    
flag = isOdd(A[0])

for num in A:
    result = isOdd(num)
    if result == flag:
        ans += 1
        flag = not result
    else:
        continue


# print(A)
print(ans)