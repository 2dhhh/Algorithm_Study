import sys

input = sys.stdin.readline

n = int(input())
ls = [0] * 1001
prefix_max = [0] * 1111
suffix_max = [0] * 1111

for _ in range(n):
  a, b = map(int, input().split())
  ls[a] = b


ans = 0
for i in range(1, 1001):
  prefix_max[i] = max(prefix_max[i-1], ls[i])

for i in range(1001)[::-1]:
  suffix_max[i] = max(suffix_max[i+1], ls[i])

for i in range(1001):
  ans += min(prefix_max[i], suffix_max[i])

print(ans)

