#1번을 해보세요!
def factorial(a):
    val = a
    for i in range(1,a):
        a = a-1
        val = val*a
    return(val)

print(factorial(5))