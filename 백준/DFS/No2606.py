import sys
input = sys.stdin.readline

def dfs(cur):
  global cnt
  cnt += 1
  visited[cur] = True
  for nxt in graph[cur]:
    if visited[nxt]:
      continue
    dfs(nxt)


n = int(input())
m = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
cnt = 0
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
print(cnt -1)