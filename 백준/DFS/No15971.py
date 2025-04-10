import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(cur):
  global ans, large
  visited[cur] = True
  if cur == y:
    return True
  for nxt, wgt in graph[cur]:
    if visited[nxt]:
      continue
    if dfs(nxt):
      ans += wgt
      large = max(large, wgt)
      return True
  return False

n, x, y = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
ans = 0
large = 0

for _ in range(n - 1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

dfs(x)
print(ans - large)