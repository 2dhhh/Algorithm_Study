import sys

input = sys.stdin.readline

# 입력
ls = [int(input()) for _ in range(10)]

sum = 0
ans = 0

for i in range(10):
  sum += ls[i]
  if abs(sum-100) <= abs(sum-ls[i]-100):
    ans = sum

  else:
    break

print(ans)
