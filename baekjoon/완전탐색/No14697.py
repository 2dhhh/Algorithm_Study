import sys

input = sys.stdin.readline

A,B,C,N = map(int, input().split())
flag = False
ans = 0

for i in range(301):
  for j in range(151):
    for k in range(101):
      if A*i + B*j + C*k == N:
        ans = 1
        flag = True
        break
    if flag:
      break
  if flag:
    break
print(ans)