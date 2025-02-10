import sys

input = sys.stdin.readline

n = int(input())

ls = list(map(int, input().split()))

s, e = 0, n-1
ans = int(1e10)
ans_s, ans_e = s, e-1

while(s < e):
  sum = ls[s] + ls[e]

  if abs(sum) < abs(ans):
    ans = sum
    ans_s = s
    ans_e = e

  if sum < 0:
    s += 1

  elif sum > 0:
    e -= 1
  else :
    break

print(ls[ans_s], ls[ans_e])
