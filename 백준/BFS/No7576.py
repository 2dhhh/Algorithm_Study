import sys
from collections import deque
input = sys.stdin.readline

dxy = [(-1, 0), (1, 0) , (0, 1), (0, -1)]
m, n = map(int ,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()
day = 0
# 익은 토마토 큐에 삽입
for i in range(n):
  for j in range(m):
    if board[i][j] == 1:
      q.append((i, j))


while q:
  sz = len(q)

  for _ in range(sz):
    x, y = q.popleft()
    for dx, dy in dxy:
      nx ,ny = x + dx, y + dy
      # 범위 체크
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 토마토가 없는 경우 혹은 이미 익은 경우
      if board[nx][ny] != 0:
        continue
      q.append((nx, ny))
      board[nx][ny] = 1

  day += 1

for i in range(n):
  for j in range(m):
    if board[i][j] == 0:
      print(-1)
      exit(0)

print(day - 1)
