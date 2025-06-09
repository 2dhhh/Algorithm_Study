import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))

dist = [int(1e9)] * (n + 1)
q = []
heapq.heappush(q, (0,k))
dist[k] = 0
while q:
  dist_x, x = heapq.heappop(q)

  if dist_x != dist[x]:
    continue

  for nxt, cost in graph[x]:
    if dist[nxt] > dist[x] + cost:
      dist[nxt] = dist[x] + cost
      heapq.heappush(q, (dist[nxt], nxt))

for i in range(1, n + 1):
  print(dist[i] if dist[i] != int(1e9) else "INF")