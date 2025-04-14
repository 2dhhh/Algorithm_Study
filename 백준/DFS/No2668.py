import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(cur):
  if not visited[cur]:
    visited[cur] = True
    for nxt in graph[cur]:
      top.add(cur)
      bottom.add(nxt)

      if top == bottom:
        ans.extend(list(top))
        return
      dfs(nxt)


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n+1):
  graph[i].append(int(input()))

ans = []

for i in range(1, n + 1):
  visited = [False] * (n + 1)
  top = set()
  bottom = set()
  dfs(i)

ans = list(set(ans))
ans.sort()
print(len(ans))
for x in ans:
  print(x)