import sys

input = sys.stdin.readline

def recur(depth, start):
  if depth == m:
    print(*selected)
    return

  for i in range(start, n):
    selected[depth] = ls[i]
    recur(depth + 1, i)


n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
selected = [0] * m
recur(0, 0)

