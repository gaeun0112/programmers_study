s = input()
answer_one=0
for i in s.split('0'):
  if i!='':
    answer_one+=1

answer_zero=0
for i in s.split('1'):
  if i!='':
    answer_zero+=1

print(min(answer_one, answer_zero))