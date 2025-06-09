import sys

input = sys.stdin.readline

def recur(depth,):
  if depth == m:
    print(*selected)
    return

  for i in range(1, n + 1):
    if visited[i]:
      continue
    selected[depth] = i
    visited[i] = True
    recur(depth + 1)
    visited[i] = False


n, m = map(int, input().split())
selected = [0] * m
visited = [False] * (n + 1)
recur(0)