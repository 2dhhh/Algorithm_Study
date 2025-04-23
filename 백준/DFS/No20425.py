import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(cur, prev):
  for nxt, mul in graph[cur]:
    if nxt != prev:
      if depth[nxt] == 0:
        depth[nxt] = depth[cur] + 1
        dfs(nxt, cur)
      # 사이클인 경우
      elif depth[nxt] < depth[cur]:
        ls.append(depth[cur] - depth[nxt] + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n +1)]
depth = [0] * (n + 1)
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b,c))
  graph[b].append((a,c))
# 사이클의 크기 저장
ls = []
for i in range(1, n+1):
  if depth[i] == 0:
    dfs(i, 0)

ans = 0
for num in ls:
  sum = num * num
  ans += sum

print(ans)



