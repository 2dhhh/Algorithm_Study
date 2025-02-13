import sys

input = sys.stdin.readline

def solution(var):
  cnt = 0
  for arr in ls:
    num = min(var, arr[1])
    if num < arr[0]:
      cnt += 0
    else :
      cnt += ((num - arr[0]) // arr[2]) + 1

  return cnt


n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

s ,e = 1, 2147483649
ans = -1

while s <= e:
  mid = (s+e)//2

  if solution(mid) % 2 == 0:
    s = mid + 1

  else :
    ans = mid
    e = mid -1


if ans == -1:
  print("NOTHING")

else :
  print(ans, solution(ans) - solution(ans-1))