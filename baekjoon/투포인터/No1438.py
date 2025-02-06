import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
points = []
x_dict = defaultdict(list)

check = n // 2
ans = int(1e10)

# 점 입력 받기
for _ in range(n):
  x, y = map(int, input().split())
  points.append((x, y))
  x_dict[x].append(y)

# X 좌표 정렬
x_keys = sorted(list(set([x for x, _ in points])))

for i in range(len(x_keys)):
  temp_y = []  # Y 좌표를 수집할 리스트
  for j in range(i, len(x_keys)):

    temp_y.extend(x_dict[x_keys[j]])
    temp_y.sort()

    if len(temp_y) >= check:
      for k in range(len(temp_y) - check + 1):
        width = x_keys[j] - x_keys[i] + 2
        height = temp_y[k + check - 1] - temp_y[k] + 2
        ans = min(ans, width * height)

print(ans)