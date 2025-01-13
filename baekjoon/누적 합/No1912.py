import sys

input = sys.stdin.readline

n = int(input())

ls = [0] + list(map(int, input().split()))

prefix_sum = [0] * (n+1)

max_value = -1000
min_value = 0



# 누적 힙 배열
for i in range(1, n+1):
  prefix_sum[i] = prefix_sum[i-1] + ls[i] # ex [0, 10, 6, 9, 10, 15, 21, -14, -2, 19]


for i in range(1, n+1):
  max_value = max(max_value, prefix_sum[i] - min_value)

  if min_value > prefix_sum[i]:
    min_value = prefix_sum[i]

print(max_value)









