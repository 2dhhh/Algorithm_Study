import sys
input = sys.stdin.readline

N = int(input())

ls = [int(input()) for _ in range(N)]

ans = 1
cnt = 1

for i in range(N):
  _remove = ls[i]
  _compare = -1
  for j in range(N):
    _tmp = ls[j]
    if _tmp == _remove:
      continue

    if _tmp == _compare:
      cnt += 1


    else:
      cnt = 1

    _compare = _tmp
    ans = max(ans, cnt)

print(ans)