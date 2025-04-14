import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y, depth):
  global ans
  ans = max(ans, depth)

  for dx, dy in dxy:
    nx, ny = x + dx, y + dy
    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
      visited.add(board[nx][ny])
      dfs(nx, ny, depth + 1)
      visited.remove(board[nx][ny])

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
dxy = [(1,0), (-1,0), (0,-1), (0,1)]
visited = set()
visited.add(board[0][0])
ans = 1

dfs(0, 0, 1)
print(ans)