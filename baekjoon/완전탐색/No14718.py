import sys

input = sys.stdin.readline

N, K = map(int, input().split())
power_list = []
speed_list = []
intel_list = []

tmp_list = [[0,0,0]]*N

for i in range(N):
  tmp_list[i] = list(map(int, input().split()))
  power_list.append(tmp_list[i][0])
  speed_list.append(tmp_list[i][1])
  intel_list.append(tmp_list[i][2])

# 리스트 정렬
min_stat = 3_000_000
cnt = 0

for i in power_list:
  for j in speed_list:
    for k in intel_list:
      for l in range(N):
        if tmp_list[l][0] <= i and tmp_list[l][1] <= j and tmp_list[l][2] <= k:
          cnt += 1

      if cnt >= K:
        min_stat = min(min_stat, i+j+k)


      cnt = 0

print(min_stat)
