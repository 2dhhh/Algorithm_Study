import sys

input = sys.stdin.readline

N = int(input())

height = [0] * 1001

for i in range(N):
  a,b = map(int, input().split())
  height[a] = b

idx = height.index(max(height))
mx = ans = 0

for i in range(idx):
  if mx < height[i]:
    mx = height[i]
  ans += mx

mx = 0
for i in range(1000, idx, -1):
  if mx < height[i]:
    mx = height[i]
  ans += mx

print(ans + height[idx])





