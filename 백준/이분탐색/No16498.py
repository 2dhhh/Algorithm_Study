import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
# A 카드
ls_a = list(map(int, input().split()))
# B 카드
ls_b = list(map(int, input().split()))
# C 카드
ls_c = sorted(list(map(int, input().split())))

ans = int(1e9)

for i in ls_a:
  for j in ls_b:
    s, e = 0, c - 1
    r = max(i, j)
    l = min(i, j)
    while s <= e:
      mid = (s + e) // 2
      if l <= ls_c[mid] <= r:
        ans = min(ans, r - l)
        break

      elif ls_c[mid] > r:
        ans = min(ans, ls_c[mid] - l)
        e = mid - 1

      else:
        ans = min(ans, r - ls_c[mid])
        s = mid + 1

print(ans)