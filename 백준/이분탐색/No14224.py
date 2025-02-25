import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]
ls_x = []
ls_y = []
for x, y in ls:
  ls_x.append(x)
  ls_y.append(y)

l, cnt = int(1e10), 0
flag = False
for x_point in ls_x:
  for y_point in ls_y:
    s, e= 0, 2*int(1e9)
    check_x = x_point-1
    check_y = y_point-1

    while s <= e :
      mid = (s + e) // 2

      for x, y in ls:
        if check_x + mid > x > check_x and check_y + mid > y > check_y:
          cnt += 1

      if cnt >= k:
        l = min(l, mid)
        e = mid - 1
        flag = True

      else:
        s = mid + 1

      cnt = 0
if not flag:
  print(2_000_000_002 * 2_000_000_002)
else:
  ans = l * l
  print(ans)