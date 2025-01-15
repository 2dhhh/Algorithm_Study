import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ls = [list(map(int,input().split())) for _ in range(n)]

prefix_2d_sum = [[0]*(m+1) for _ in range(n+1)]


for i in range(1, n+1):
  for j in range(1, m+1):
    prefix_2d_sum[i][j] = prefix_2d_sum[i-1][j] + prefix_2d_sum[i][j-1] - prefix_2d_sum[i-1][j-1] + ls[i-1][j-1]

ans = -10000

for i in range(1, n+1):
  for j in range(1, m+1):
    for p in range(i, n+1):
      for q in range(j, m+1):
        ans = max(ans, prefix_2d_sum[p][q] - prefix_2d_sum[p][j-1] - prefix_2d_sum[i-1][q] + prefix_2d_sum[i-1][j-1])

print(ans)


