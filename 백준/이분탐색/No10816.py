import sys

input = sys.stdin.readline

n = int(input())
ls_n = sorted(list(map(int, input().split())))

m = int(input())
ls_m = list(map(int, input().split()))

for num in ls_m:
  s, e = 0, n-1
  l = -1
  while s <= e:
    mid = (s+e) // 2
    if ls_n[mid] == num :
      l = mid
      e = mid -1

    elif ls_n[mid] > num :
      e = mid -1
    else :
      s = mid + 1

  s,e = 0, n-1
  r = -1
  while s <= e:
    mid = (s+e) // 2
    if ls_n[mid] == num:
      r = mid
      s = mid + 1
    elif ls_n[mid] < num:
      s = mid + 1
    else :
      e = mid - 1

  if r == -1 or l == -1:
    print(0, end =" ")
  else :
    print(r-l+1, end = " ")

# import sys
# from collections import defaultdict
# input = sys.stdin.readline
#
# n = int(input())
# ls_n = list(map(int, input().split()))
#
# m = int(input())
# ls_m = list(map(int, input().split()))
#
# dd = defaultdict(int)
#
# for num in ls_n:
#   dd[num] += 1
#
# ls_cnt = [0] * m
# for i in range(m):
#   num = ls_m[i]
#   ls_cnt[i] = dd[num]
#
# print(*ls_cnt)


