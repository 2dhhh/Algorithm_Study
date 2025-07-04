import sys

input = sys.stdin.readline

def recur(k, cnt):
  # 배열의 끝
  if k == n + 1:
    if cnt == m:
      print(*selected)
    return

  else:
    selected.append(k)
    # 고를래?
    recur(k + 1, cnt + 1)
    selected.pop()
    # 말래 ?
    recur(k + 1, cnt)


n, m = map(int, input().split())
selected = []
recur(1, 0)
