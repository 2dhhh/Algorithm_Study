import sys

input = sys.stdin.readline

n, k = map(int, input().split())

ls = list(map(int, input().split()))

prefix_dict = {0: 1}

# 누적 합
prefix_sum = 0

ans = 0

for num in ls:
  prefix_sum += num

  if (prefix_sum - k) in prefix_dict:
    ans += prefix_dict[prefix_sum - k]

  prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

print(ans)