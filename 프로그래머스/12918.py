def solution(s):
  print(s.isdigit())
  print(len(s))
  if len(s) != 4 and len(s) != 6:
    answer = False
    print('here')
    return answer
  answer = s.isdigit()
  print('good')
  return answer
