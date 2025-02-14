import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
cnt = 0
dict = defaultdict(list)
ls = [list(map(int, input().split())) for _ in range(n)]

for x,y in ls:
  dict[x].append(y)

for x, y in ls:
  if y+b in dict[x] and y in dict[x+a] and y+b in dict[x+a]:
    cnt += 1
print(cnt)