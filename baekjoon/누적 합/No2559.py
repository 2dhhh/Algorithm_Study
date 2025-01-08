import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ls = [0] + list(map(int, input().split()))

p_sum = [0] * (N+1)

ans = -100_000_000

# 누적 합 배열 초기화
for i in range(1,N+1):
  p_sum[i] = p_sum[i-1] + ls[i]

for i in range(N+1):
  if i + K <= N:
    ans = max(p_sum[i+K] - p_sum[i], ans)

print(ans)
