N = int(input())
A = list(map(int, input().split()))
Answer = 0

def settings():
    global Answer
    A.append(A[0])
    for i in range(N):
        if A[i] >= A[i + 1]:
            Answer += 1

settings()
print(Answer)
