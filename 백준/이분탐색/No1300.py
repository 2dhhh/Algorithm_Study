import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
ans = -1
s, e = 1, k

while s <= e:
  mid = (s + e) // 2 # 정답의 후보
  cnt = 0
  for i in range(1, n+1):
    cnt += min(n, mid//i)

  if cnt >= k:
    ans = mid
    e = mid - 1
  else:
    s = mid + 1

print(ans)