import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dist_start_x = [int(1e6)] * (n + 1)
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

q = []
heapq.heappush(q, (0, x))
dist_start_x[x] = 0
while q:
  dist_s, s = heapq.heappop(q)

  if dist_start_x[s] != dist_s:
    continue

  for nxt, cost in graph[s]:

    if dist_start_x[nxt] > dist_s + cost:
      dist_start_x[nxt] = dist_s + cost
      heapq.heappush(q, (dist_start_x[nxt], nxt))

ans = -1

for i in range(1, n + 1):
  dist = [int(1e6)] * (n + 1)
  p = []
  heapq.heappush(p, (0, i))
  dist[i] = 0
  while p:
    dist_e, e = heapq.heappop(p)

    if dist[e] != dist_e:
      continue

    for nxt, cost in graph[e]:

      if dist[nxt] > dist_e + cost:
        dist[nxt] = dist_e + cost
        heapq.heappush(p, (dist[nxt], nxt))

  ans = max(ans, dist[x] + dist_start_x[i])

print(ans)
