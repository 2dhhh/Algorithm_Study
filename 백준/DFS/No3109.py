import sys

input = sys.stdin.readline

def dfs(cur,t,cnt):
  visited[cur][t] = True
  global ans

  for dx,dy in dxy:
    ddx = cur + dx
    ddy = t + dy
    if ddx >= r or ddy >= c:
      continue
    if ddy == c-1:
      ans = max(ans, cnt)
      return cnt

    if board[ddx][ddy] == 'x':
      cnt += 1

    dfs(ddx, ddy, cnt)

r, c = map(int, input().split())
board = []
visited = [[False]*c for _ in range(r)]
ans = 0
dxy = [(0,1), (1, 1),(-1,1)]

for _ in range(r):
  board.append(list(input().strip()))

for i in range(r):
  dfs(i,0, 0)

print(ans)