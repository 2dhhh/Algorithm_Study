import sys
from collections import deque
input = sys.stdin.readline

n ,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = (-int(1e9))

for i in range(n):
  for j in range(m):
    if board[i][j] == 'W':
      continue
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    dist[i][j] = 0

    while q:
      x, y = q.popleft()
      for dx, dy in dxy:
        nx, ny = x + dx , y + dy
        # 범위 체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          continue

        # 방문 체크
        if dist[nx][ny] != -1:
          continue

        if board[nx][ny] == 'W':
          continue

        q.append((nx,ny))
        dist[nx][ny] = dist[x][y] + 1
        ans = max(ans, dist[nx][ny])

print(ans)