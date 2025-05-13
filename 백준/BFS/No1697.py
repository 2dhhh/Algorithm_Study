import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 200001
dist = [-1] * 200001
q = deque()
q.append(n)
visited[n] = True
dist[n] = 0

while q:
  cur = q.popleft()

  for nxt in [cur -1, cur + 1, cur * 2]:
    if nxt < 0 or nxt > 100000:
      continue
    if visited[nxt]:
      continue
    q.append(nxt)
    visited[nxt] = True
    dist[nxt] = dist[cur] + 1

print(dist[k])