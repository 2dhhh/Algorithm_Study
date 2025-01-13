import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(n)]
prefix_2d_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1,n+1):
    prefix_2d_sum[i][j] = prefix_2d_sum[i-1][j] + prefix_2d_sum[i][j-1] - prefix_2d_sum[i-1][j-1] + ls[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(prefix_2d_sum[x2][y2] - prefix_2d_sum[x1-1][y2] - prefix_2d_sum[x2][y1-1] + prefix_2d_sum[x1-1][y1-1])
