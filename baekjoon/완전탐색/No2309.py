import sys

input = sys.stdin.readline

ls = sorted(int(input()) for _ in range(9))

sum = 0
idx1 = 0
idx2 = 0
flag = False


for i in range(9):
  sum += ls[i]

for i in range(9):
  for j in range(1,9):
    if ls[i] + ls[j] == sum - 100:
      idx1 = i
      idx2 = j
      flag = True
      break

  if flag:
    break

for i in range(9):
  if i == idx1 or i == idx2:
    continue
  else:
    print(ls[i])






