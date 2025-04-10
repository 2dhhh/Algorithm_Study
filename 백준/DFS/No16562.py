import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(cur):
  visited[cur] = True
  global min_cost
  min_cost = min(min_cost, cost[cur])
  for nxt in graph[cur]:
    if not visited[nxt]:
      dfs(nxt)

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
ans = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n + 1):
  if not visited[i]:
    min_cost = cost[i]
    dfs(i)
    ans += min_cost

print("Oh no" if ans > k else ans)