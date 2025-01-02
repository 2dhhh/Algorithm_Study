import sys

input = sys.stdin.readline

N = int(input())
S = [int(input()) for _ in range(N)]



for i in S:
  ans = "YES"
  for j in range(2, 1000001):
    if i % j == 0:
      ans = "NO"
      break
  print(ans)