import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

l = 0
odd_cnt = 0
ans = 0

for r in range(n):
  # 홀수 일 때
  if ls[r] % 2 != 0:
    odd_cnt += 1

  while odd_cnt > k:
    if ls[l] % 2 != 0:
      odd_cnt -=1
    l += 1

  ans = max(ans, r-l+1 - odd_cnt)

print(ans)