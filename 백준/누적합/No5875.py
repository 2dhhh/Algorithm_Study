import sys

input = sys.stdin.readline

n = input().strip()
num = len(n)

ls = [0] * (num+1)
# 왼쪽 누적합
prefix_sum = [0] * (num+1)
# 오른쪽 누적합
suffix_sum = [0] * (num+2)
left = right = 0

for i in range(0,num):
  if n[i] == '(':
    ls[i+1] = 1
    left += 1
  else:
    ls[i+1] = -1
    right += 1

# '(' 더 많은 경우
if left > right:
  left = 0
  for i in range(num, 0, -1):
    if ls[i] == 1:
      left += 1
    suffix_sum[i] = suffix_sum[i+1] + ls[i]
    # 처음으로 1이 나오는 경우
    if suffix_sum[i] == 1:
      print(left)
      break

# ')' 더 많은 경우
elif right > left :
  right = 0
  for i in range(1, num+1):
    if ls[i] == -1:
      right += 1
    prefix_sum[i] = prefix_sum[i-1] + ls[i]
    # 처음으로 -1이 나오는 경우
    if prefix_sum[i] == -1:
      print(right)
      break

# 개수가 같은 경우
else :
  print(0)
