import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(int(input()) for _ in range(m))
ans = 0

s ,e = 1, 1_000_000_000

def check(x):
  num = 0
  for i in range(m):
    num += ls[i] // x
    if ls[i] % x :
      num += 1
  return num <= n

while s <= e:
  mid = (s + e) // 2

  if check(mid):
    ans = mid
    e = mid -1

  else :
    s = mid + 1
print(ans)