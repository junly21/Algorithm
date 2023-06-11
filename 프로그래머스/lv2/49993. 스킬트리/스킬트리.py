def ispossible(skill, skillset):
    success = 0
    order = 0
    skill_list = []
    for target in skill:
        skill_list.append(target)
    #찾을 대상target skillset반복문 돌면서 몇번째인지 찾아
    for target in skill_list: # C B D
        find = 0 
        change = 0
        for s in skillset: # BACDE체크
            if s in skill and s != skill_list[0]:
                return 0
            elif s in skill and s == skill_list[0]:
                skill_list.pop(0)
        return 1
                
                
def solution(skill, skill_trees):
    answer = 0
        
    for skill_tree in skill_trees:   #스킬트리 한개만 분석 
        skillset = []
        
        for skills in skill_tree: #스킬트리 한개 안의 여러스킬
            skillset.append(skills) #리스트화
            
        issuccess = ispossible(skill, skillset) #판별함수
        if issuccess == 1:
            answer += 1
    
    return answer