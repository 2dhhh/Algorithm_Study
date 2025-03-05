import sys

input = sys.stdin.readline

def dfs(x, count):
  global flag
  visited[x] = True
  if x==b:
    flag=True
    print(count)
  for nxt in graph[x]:
    if visited[nxt]:
      continue
    dfs(nxt,count+1)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n + 1)
flag = False
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(a,0)
if not flag:
  print(-1)