import sys

input = sys.stdin.readline

h, w = map(int, input().split())

ls = [0] + list(map(int, input().split()))

prefix_max = [0] * (w+2)
suffix_max = [0] * (w+2) # 마지막 인덱스는 W+1

for i in range(1,w+1):
  prefix_max[i] = max(prefix_max[i-1], ls[i])

for i in range(1, w+1)[::-1]:
  suffix_max[i] = max(suffix_max[i+1], ls[i])

ans = 0
for i in range(1, w+1):
  tmp = min(prefix_max[i], suffix_max[i])
  if ls[i] < tmp:
    ans += tmp-ls[i]

print(ans)


