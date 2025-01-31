import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
r = -1
total = 0
ans = 0
for l in range(n):
  while r + 1 < n  and total < m:
    r += 1
    total += ls[r]
  if total == m:
    ans += 1
  total -= ls[l]
print(ans)