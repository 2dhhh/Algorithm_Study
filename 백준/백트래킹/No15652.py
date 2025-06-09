import sys

input = sys.stdin.readline

def recur(depth):
  global flag
  if depth == m:
    arr = sorted(selected)
    for i in range(len(selected)):
      if arr[i] != selected[i]:
        flag = True
    if flag:
      flag = False
      return

    print(*selected)
    return

  for i in range(1, n + 1):
    selected[depth] = i
    recur(depth + 1)

flag = False
n, m = map(int, input().split())
selected = [0] * m
recur(0)