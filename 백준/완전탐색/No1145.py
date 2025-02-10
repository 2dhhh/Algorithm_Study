import sys

input = sys.stdin.readline

# 5개의 자연수 입력
ls = list(map(int,input().split()))
ans = 0

for i in range(1, 1000000):
  cnt = 0
  for j in ls:
    if i % j ==0 :
      cnt += 1
  if cnt >= 3:
    ans = i
    break
print(ans)