import sys

input = sys.stdin.readline

N,M,L,K = map(int, input().split())

ls = [list(map(int, input().split())) for _ in range(K)]

x_points = []
y_points = []
ans = 0

for x,y in ls:
  x_points.append(x)
  y_points.append(y)

for i in range(K):
  for j in range(K):
    cnt = 0
    _x = x_points[i]
    _y = y_points[j]

    for k in range(K):
      if _x <= ls[k][0] <= _x+L and _y <= ls[k][1] <= _y+L:
        cnt += 1
    ans = max(ans, cnt)

print(K-ans)


