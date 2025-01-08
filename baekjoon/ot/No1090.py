import sys

input = sys.stdin.readline

N = int(input())

# 체커의 좌표
ls = [list(map(int, input().split())) for _ in range(N)]

x_points = []
y_points = []

ans = [-1] *N

# x좌표 y좌표 분리
for i in range(N):
  x_points.append(ls[i][0])
  y_points.append(ls[i][1])

for sx in x_points:
  for sy in y_points:
    dist = []
    # 특정위치의 좌표에서 체커들 사이의 거리를 저장
    for x,y in ls:
      distance = (abs(sx-x) + abs(sy-y))
      dist.append(distance)

    # 오름차순 정렬
    dist.sort()

    temp = 0
    for i in range(len(dist)):
      distance = dist[i]
      temp += distance
      if ans[i] == -1 :
        ans[i] = temp
      else:
        ans[i] = min(temp, ans[i])
print(*ans)