n = int(input())

n = str(n)
x=0
y=0
for i in n[0:int(len(n)/2)]:
  x+=int(i)
for i in n[int(len(n)/2):]:
  y+=int(i)

if x==y:
  print("LUCKY")
else:
  print("READY")