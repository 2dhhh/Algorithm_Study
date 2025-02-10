import sys

input = sys.stdin.readline

# 색종이 수
n = int(input())

# 입력 받은 x,y 좌표 값 리스트
ls = [list(map(int, input().split())) for _ in range(n)]

# 100x100 도화지 배열 선언
sk = [[False for j in range(101)] for i in range(101)]
cnt = 0

for i in ls:
  x = i[0]
  y = i[1]
  for j in range(10):
    for k in range(10):
      sk[x][y] = True
      x += 1
    y +=1
    x = i[0]

for i in range(101):
  for j in range(101):
    if sk[i][j]:
      cnt += 1

print(cnt)
