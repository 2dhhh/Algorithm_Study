import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [[0] * (m + 1)]
for i in range(1, n + 1):
  ls = [0] + list(map(int, input().rstrip()))
  board.append(ls)

dist = [([int(1e5)] * (m + 1)) for _ in range(n + 1)]
q = deque()
q.append((1, 1))
dist[1][1] = 0


while q:
  x, y = q.popleft()

  for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    nx, ny = x + dx, y + dy

    if nx < 1 or ny < 1 or nx > m or ny > n:
      continue

    # 벽일 경우
    if board[ny][nx] == 1:
      if dist[ny][nx] > dist[y][x] + 1:
        dist[ny][nx] = dist[y][x] + 1
        q.append((nx,ny))


    else:
      if dist[ny][nx] > dist[y][x]:
        dist[ny][nx] = dist[y][x]
        q.append((nx,ny))

print(dist[n][m])

