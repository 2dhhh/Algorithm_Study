import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for i in range(1, 501):
  for j in range(1, i):
    if i*i == j*j+N:
      cnt += 1
      break
print(cnt)