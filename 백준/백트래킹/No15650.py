import sys

input = sys.stdin.readline

def recur(depth, start):
  if depth == m:
    print(*selected)
    return
  for i in range(start, n + 1):
    selected[depth] = i
    recur(depth + 1, i + 1)

n, m = map(int, input().split())
selected = [0] * m
recur(0, 1)

# import sys
#
# input = sys.stdin.readline
#
# def recur(k, cnt):
#   # 배열의 끝
#   if k == n + 1:
#     if cnt == m:
#       print(*selected)
#     return
#
#   else:
#     selected.append(k)
#     # 고를래?
#     recur(k + 1, cnt + 1)
#     selected.pop()
#     # 말래 ?
#     recur(k + 1, cnt)
#
#
# n, m = map(int, input().split())
# selected = []
# recur(1, 0)
