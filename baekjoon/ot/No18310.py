import sys


input = sys.stdin.readline


N = int(input())
ls = sorted(map(int, input().split()))

if N % 2 == 0:
  print(ls[N//2 -1])

else:
  print(ls[(N//2)])





