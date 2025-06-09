# 백준_1132_ 부분수열의 합

import sys

input = sys.stdin.readline

def recur(cur, total):
  global cnt

  # 배열의 끝 도착
  if cur == n:
    if total == m:
      cnt += 1
    return

  # 고를래?
  recur(cur + 1, total + ls[cur])

  # 말래?
  recur(cur + 1, total)

n, m = map(int, input().split())
ls = list(map(int, input().split()))
cnt = 0
recur(0, 0)
#공집합인 경우 빼줘야함
print(cnt - int(m == 0))