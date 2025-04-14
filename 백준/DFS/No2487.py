import sys
import math

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(cur):
  visited[cur] =True
  cnt = 1
  for nxt in graph[cur]:
    if visited[nxt]:
      continue
    cnt += dfs(nxt)
  return cnt

n = int(input())
graph = [[] for _ in range(n + 1)]
ls = list(map(int, input().split()))
visited = [False] * (n + 1)
tmp = 0
for num in ls:
  tmp += 1
  graph[tmp].append(num)

gcd = []
for i in range(1, n + 1):
  if visited[i]:
    continue
  num = dfs(i)
  gcd.append(num)
print(math.lcm(*gcd))


