import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [[0] * (m+1)] + [[0] + list(map(int, input().strip())) for _ in range(n)]

prefix = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, m+1):
    if matrix[i][j] == 0:
      prefix[i][j] = prefix[i-1][j] + 1

ans = 0

for i in range(1, n+1):
  for j in range(1, m+1):
    tmp = 334
    if prefix[i][j] == 0:
      continue
    for k in range(j,0, -1):
      if prefix[i][k] < tmp:
        tmp = prefix[i][k]

      if tmp * (j-k +1) > ans:
        ans = tmp * (j-k +1)

print(ans)


