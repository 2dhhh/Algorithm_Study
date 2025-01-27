import sys

input = sys.stdin.readline

n = int(input())
ls = sorted(list(map(int, input().split())))
x = int(input())

s = 0
e = n-1
cnt = 0

while (s < e):
  if ls[s] + ls[e] == x:
    cnt += 1
    s += 1
    e -= 1
  elif ls[s] + ls[e] > x:
    e -= 1
  else :
    s += 1

print(cnt)