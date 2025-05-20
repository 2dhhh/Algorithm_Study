import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [-1] * 100001
prev = [-1] * 100001
q = deque()
q.append(n)
dist[n] = 0
while q:
  cur = q.popleft()

  for nxt in [cur - 1, cur + 1, cur * 2]:
    if nxt < 0 or nxt > 100000:
      continue

    if dist[nxt] != -1:
      continue
    q.append(nxt)
    dist[nxt] = dist[cur] + 1
    prev[nxt] = cur

print(dist[k])

ans = [k]
idx = k
while prev[idx] != -1:
  ans.append(prev[idx])
  idx= prev[idx]
print(*ans[::-1])

