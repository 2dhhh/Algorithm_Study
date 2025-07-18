import sys

input = sys.stdin.readline

def recur(depth):
  if depth == m:
    print(*selected)
    return

  for i in range(1, n + 1):
    selected[depth] = i
    recur(depth + 1)


n, m = map(int ,input().split())
selected = [0] * m
recur(0)