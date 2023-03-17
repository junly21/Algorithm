def solution(answers):
  answers=[]
  std1 = [1,2,3,4,5]
  std2 = [2,1,2,3,2,4,2,5]
  std3 = [3,3,1,1,2,2,4,4,5,5]
  score = [0,0,0]
  for idx, i in enumerate(answers):
    if i==std1[idx%5]:
      score[0] += 1
    if i==std2[idx%8]:
      score[1] += 1
    if i==std3[idx%10]:
      score[3] += 1

    max_score = max(score)

    for i in score:
      if i ==max_score:
        answers.append(i+1)
        


  return answers