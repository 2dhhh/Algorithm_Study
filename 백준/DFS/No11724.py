import sys

input =sys.stdin.readline

def dfs(cur):
  visited[cur] = True
  for nxt in graph[cur]:
    if visited[nxt]:
      continue
    dfs(nxt)

n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cnt = 0
for i in range(1, n+1):
  if visited[i]:
    continue
  cnt += 1
  dfs(i)
print(cnt)