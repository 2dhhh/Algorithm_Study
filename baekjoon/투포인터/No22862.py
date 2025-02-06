import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

r = -1
odd_cnt = 0
ans = 0

for l in range(n):
  while r + 1 < n and odd_cnt <= k:
    r += 1
    if ls[r] % 2 != 0:
      odd_cnt += 1

  if odd_cnt > k:
    if ls[l] % 2 != 0:
      odd_cnt -= 1

  ans = max(ans, r - l + 1 - odd_cnt)

print(ans)