import sys
from collections import deque
input = sys.stdin.readline
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
q = deque()
for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      q.append((i,j))
      cnt += 1
    if cnt == (n + 1) * (m + 1):
      print(0)
      exit()

dist = 0
while q:
  sz =len(q)

  for _ in range(sz):
    x, y = q.popleft()
    for dx, dy in dxy:
      nx, ny = x + dx, y + dy
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if board[nx][ny] != 0:
        continue
      board[nx][ny] = 1
      q.append((nx, ny))
  dist += 1

for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      print(-1)
      exit()

print(dist -1)