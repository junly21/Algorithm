N = int(input())
i=0
count =0
while True:
    count += 1
    i += count
    if i >= N:
        if count % 2 == 0:
            up = (i-N+1)
            down = (count-i+N)
            print(down,"/",up,sep="")
            break
        else:
            up = (i-N+1)
            down = (count-i+N)
            print(up,"/",down,sep="")
            break
   