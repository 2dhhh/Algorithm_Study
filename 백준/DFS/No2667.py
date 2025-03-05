import sys

input = sys.stdin.readline

def dfs(x, y):
  visited[x][y] = True
  sz = 1
  for dx, dy in dxy:
    nx, ny = x + dx, y + dy
    # 범위 체크
    if nx >= n or nx < 0 or ny >= n or ny < 0:
      continue
    if board[nx][ny] == 0:
      continue
    if visited[nx][ny]:
      continue
    sz += dfs(nx, ny)
  return sz

n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]

dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

visited = [[False] * n for _ in range(n)]

cnt = 0
ls = []

for i in range(n):
  for j in range(n):
    if board[i][j] == 0:
      continue
    if visited[i][j]:
      continue
    ls.append(dfs(i,j))
    cnt += 1

ls.sort()
print(cnt)
for i in ls:
  print(i)