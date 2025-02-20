import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(int(input()) for _ in range(n))

s, e = 1, max(ls)
ans = 0

while s <= e:
  mid = (s + e) // 2
  cnt = 0

  for num in ls:
    if num >= mid:
      cnt += num // mid

  if cnt >= k:
    ans = max(ans, mid)
    s = mid + 1
  else :
    e = mid -1
print(ans)
