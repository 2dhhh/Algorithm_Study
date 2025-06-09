import sys
from collections import deque
input = sys.stdin.readline

n, T = map(int, input().split())
ls = set()
for _ in range(n):
  a, b = map(int, input().split())
  ls.add((a,b))

q = deque()
q.append((0,0,0))

while q:
  x, y, dist = q.popleft()
  if y == T:
    print(dist)
    exit()

  for i in range(-2, 3):
    for j in range(-2, 3):
      nx = x + i
      ny = y + j
      if (nx, ny) in ls:
        q.append((nx, ny, dist + 1))
        ls.remove((nx,ny))

print(-1)