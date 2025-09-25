import sys

input = sys.stdin.readline

def dfs(x, y, depth):
  global ans
  ans = max(ans, depth)

  for dx, dy in dxy:
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= r or ny < 0 or ny >= c:
      continue

    if board[nx][ny] in visited:
      continue

    visited[nx][ny].add(board[nx][ny])
    dfs(nx, ny, depth + 1)
    visited.remove(board[nx][ny])



dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
visited = set()
ans = 1

dfs(0, 0, 1)
print(ans)


