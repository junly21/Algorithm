#1번을 해보세요!
value = int(input())

def sum_func(v):
    add=0
    for i in range(1,v+1):
        add += i
    return add

print(sum_func(value))