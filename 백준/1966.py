N = int(input())

doc_num = []
doc_location = []
docs = []
importance = []
for i in range(N): #테스트케이스 수  만큼 이하 과정 반복1
    a, b = map(int,input().split()) #첫 줄에 두 수 입력받기
    doc_num.append(a) #몇개의 문서중
    doc_location.append(b) #찾을 문서의 인덱스
    temp_list = list(map(int,(input().split())))
    importance.append([])
    for j in range(len(temp_list)):
        importance[i].append(temp_list[j])
    



print(doc_num)
print(doc_location)
print(importance)