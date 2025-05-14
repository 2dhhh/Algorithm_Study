import sys
from collections import deque

input = sys.stdin.readline
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, m = map(int, input().split())
board = [[0] * (m + 1)]
dist = [([-1] * (m + 1)) for _ in range(n + 1)]
for i in range(n):
  ls = [0] + list(map(int, input().strip()))
  board.append(ls)
q = deque()
q.append((1,1))
dist[1][1] = 1

while q:
  x, y = q.popleft()
  for dx, dy in dxy:
    nx, ny = x + dx, y + dy
    # 범위 체크
    if nx < 1 or nx > n or ny < 1 or ny > m:
      continue
    if dist[nx][ny] != -1:
      continue
    if board[nx][ny] == 0:
      continue
    q.append((nx, ny))
    dist[nx][ny] = dist[x][y] + 1
print(dist[n][m])

