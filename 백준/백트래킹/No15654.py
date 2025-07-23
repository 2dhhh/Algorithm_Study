import sys
from collections import defaultdict


input = sys.stdin.readline

def recur(depth):
  if depth == m:
    print(*selected)
    return
  for i in ls:
    if visited[i]:
      continue
    selected[depth] = i
    visited[i] = True
    recur(depth + 1)
    visited[i] = False





n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
selected = [0] * m
visited = defaultdict(bool)
recur(0)

