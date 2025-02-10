import sys

input = sys.stdin.readline

n = int(input())
ls_n = sorted(list(map(int, input().split())))

m = int(input())
ls_m = list(map(int, input().split()))

# 정답의 후보
s ,e = 0, n-1


for num in ls_m:
  ans = False
  s ,e = 0, n-1
  while s <= e :
    mid = (s + e) // 2
    if ls_n[mid] == num:
      ans = True
      break

    elif ls_n[mid] > num:
      e = mid -1

    else :
      s = mid + 1

  if ans:
    print(1, end =" ")
  else :
    print(0, end = " ")