import sys
sys.setrecursionlimit(int(1e6))
from collections import defaultdict
input = sys.stdin.readline

def dfs(cur):
  visited[cur] = True
  for nxt in graph[cur]:
    if visited[nxt]:
      continue
    dfs(nxt)


n = int(input())
ls = list(map(int, input().split()))
arr = sorted(ls)
visited = defaultdict(bool)
graph = defaultdict(list)

for i in range(n):
  if ls[i] != arr[i]:
    graph[ls[i]].append(arr[i])

cnt = 0
for cur in ls:
  if visited[cur]:
    continue
  dfs(cur)
  cnt += 1


# 결론 -> 수열의 크기 - (연결요소의 크기 혹은  사이클의 크기)
print(n - cnt)
