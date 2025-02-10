import sys

input = sys.stdin.readline
arr = [0]*1000
# 근무자 수
N = int(input())
# 근무 시간에 대한 리스트
work = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in work:
  start = i[0]
  end = i[1]
  for j in range(start, end):
    arr[j] += 1

for i in work:
  cnt = 0
  start = i[0]
  end = i[1]
  for j in range(start, end):
    arr[j] -= 1

  for j in range(1000):
    if arr[j] > 0:
      cnt += 1
  ans = max(ans, cnt)

  for j in range(start, end):
    arr[j] += 1

print(ans)
