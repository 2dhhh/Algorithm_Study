import sys

input = sys.stdin.readline

n = int(input())


ls = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[[0] * 11 for _ in range(n + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(1, 11):
      if k == ls[i][j]:
        prefix_sum[i][j][k] += 1
      prefix_sum[i][j][k] += prefix_sum[i-1][j][k] + prefix_sum[i][j-1][k] - prefix_sum[i-1][j-1][k]


q = int(input())
for _ in range(q):
  x1, y1, x2, y2 = map(int, input().split())
  ans = 0
  for k in range(1, 11):
    if prefix_sum[x2][y2][k] - prefix_sum[x2][y1 - 1][k] - prefix_sum[x1-1][y2][k] + prefix_sum[x1-1][y1-1][k]:
      ans += 1
  print(ans)