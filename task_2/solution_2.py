# your code here
user_input = input()
# your code here
a = []
n = int(input())
for i in range(n):
  new = int(input())
  a.append(new)
m = 0
most_frequent_character = 0
for x in a:
  c= a.count(x)
  if c > m:
    m = c
    most_frequent_character = x
print(most_frequent_character)
