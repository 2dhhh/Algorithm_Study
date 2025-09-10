import sys

input = sys.stdin.readline

n = int(input())

ls = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n+1)

for i in range(1, n+1):
  prefix_sum[i] = prefix_sum[i-1] + ls[i]

max_value = -int(1e8)
# 최소값 기준을 0으로 세팅하는게 핵심
min_value = 0

for i in range(1, n+1):

  max_value = max(max_value, prefix_sum[i] - min_value)

  min_value = min(min_value, prefix_sum[i])

print(max_value)
