N = int(input())

for i in range(N):
    count = 0
    docs, index = map(int,input().split()) #첫 줄에 두 수 입력받기
    doc_list = list(map(int,input().split()))
    while(max(doc_list)!=doc_list[index]):
        for j in doc_list:
            if max(doc_list) != doc_list[0]:
                temp = doc_list[0]
                for k in range(len(doc_list)-1):
                    doc_list[k] = doc_list[k+1]
                doc_list[-1] = temp
            else:
                count += 1
                doc_list.remove(max(doc_list))
        count += 1
        print(count)        