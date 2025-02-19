import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls_a = sorted(list(map(int, input().split())))
ls_b = sorted(list(map(int, input().split())))
win_a = 0
win_b = 0
draw = 0
cnt = 0

for a in ls_a:
  s, e = 0, m-1
  tmp_b = 0
  while s <= e:
    mid = (s + e) // 2
    if ls_b[mid] >= a:
      e = mid -1
    else :
      win_a += mid - tmp_b + 1
      tmp_b = mid+1
      s = mid + 1

for b in ls_b:
  s,e = 0, n-1
  tmp_a = 0
  while s <= e:
    mid = (s + e) // 2
    if ls_a[mid] >= b:
      e = mid -1
    else:
      win_b += mid - tmp_a + 1
      tmp_a = mid + 1
      s = mid + 1

draw = n*m - (win_a + win_b)
print(win_a, win_b, draw)
