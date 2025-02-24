import sys

input = sys.stdin.readline

n, c= map(int, input().split())
ls = sorted([int(input()) for _ in range(n)])

s, e = 1, ls[-1] - ls[0]
ans = 0
while s <= e:
  mid = (s + e) // 2
  start = ls[0]
  cnt = 1

  for i in range(1, len(ls)):
    if ls[i] >= start + mid:
      cnt += 1
      start = ls[i]

  if cnt >= c:
    s = mid + 1
    ans = mid

  else :
    e = mid -1

print(ans)
