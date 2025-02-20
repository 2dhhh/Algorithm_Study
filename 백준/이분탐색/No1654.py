import sys

input = sys.stdin.readline

k, n = map(int, input().split())
ls = list(int(input()) for _ in range(k))
ans = 0
s, e = 1, max(ls)
while s <= e:
  mid = (s + e) // 2
  cnt = 0
  for num in ls:
    cnt += num // mid

  if cnt >= n:
    ans = max(ans, mid)
    s = mid + 1

  else :
    e = mid - 1
print(ans)