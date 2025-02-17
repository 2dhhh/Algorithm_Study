import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
ls_a = list(map(int,input().split()))
ls_b = list(map(int,input().split()))
ls_c = sorted(list(map(int,input().split())))
ans = int(1e10)
for A in ls_a:
  for B in ls_b:
    max_v = max(A,B)
    min_v = min(A,B)
    s ,e = 0, c-1
    while s <= e:
      mid = (s+e) // 2
      if min_v <= ls_c[mid] <= max_v:
        ans = min(ans, max_v - min_v)
        break

      elif ls_c[mid] > max_v:
        ans = min(ans, ls_c[mid] - min_v)
        e = mid -1

      else:
        ans = min(ans, max_v - ls_c[mid])
        s = mid + 1

print(ans)
