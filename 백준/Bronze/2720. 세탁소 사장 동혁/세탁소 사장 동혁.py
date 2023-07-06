T = int(input())

for i in range(T):
    Quarter = 0
    Dime = 0
    Nickel = 0
    Penny = 0
    C = int(input())
    while C >= 25:
        Quarter += 1
        C -= 25
    while C >= 10:
        Dime += 1
        C -= 10
    while C>= 5:
        Nickel += 1
        C -= 5
    while C>= 1:
        Penny += 1
        C -= 1
    print(Quarter, Dime, Nickel, Penny)