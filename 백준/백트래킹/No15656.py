import sys

input = sys.stdin.readline

def recur(depth):
  if depth == m:
    print(*selected)
    return
  for num in ls:
    selected[depth] = num
    recur(depth + 1)

n, m = map(int, input().split())
ls = sorted(list(map(int, input().split())))
selected = [0] * m
recur(0)