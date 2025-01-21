import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

A_prefix_sum = [0] * (n+1)
B_prefix_sum = [0] * (n+1)

for i in range(1, n+1):
  A_prefix_sum[i] = A_prefix_sum[i-1] + A[i]
  B_prefix_sum[i] = B_prefix_sum[i-1] + B[i]

dict = defaultdict(int)
cnt = 0
for i in range(1, n+1):
  if A_prefix_sum[i] - B_prefix_sum[i] == 0:
    cnt += 1

  diff = A_prefix_sum[i] - B_prefix_sum[i]
  cnt += dict.get(diff, 0)

  if diff in dict:
    dict[diff] += 1

  else:
    dict[diff] = 1

print(cnt)
