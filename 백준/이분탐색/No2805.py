import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

s = 0
e = int(1e9)
ans = -1
while s <= e:
  mid = (s + e) // 2

  sum = 0
  for num in ls:
    if num >= mid:
      sum += num -mid

  if sum >= m:
    ans = mid
    s= mid + 1
  else :
    e = mid -1
print(ans)