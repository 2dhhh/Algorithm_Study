import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ls = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N+1)

for i in range(1,N+1):
  prefix_sum[i] = prefix_sum[i-1] + ls[i]

for i in range(M):
  start, end = map(int, input().split())
  print(prefix_sum[end] - prefix_sum[start-1])