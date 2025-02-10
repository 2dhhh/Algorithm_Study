import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for x in range(1,N-1):
  for y in range(1,N-x):
    z =  N - x - y
    if z >= y+2 and x % 2 ==0:
      cnt += 1

print(cnt)


