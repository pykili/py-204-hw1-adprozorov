# your code here
a = []
n = int(input())
for i in range(n):
  new = int(input())
  a.append(new)
c = 0
for b in a:
  if b > c:
    c = b
print(c)    
