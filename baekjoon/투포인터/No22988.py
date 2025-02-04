import sys

input = sys.stdin.readline

n , x = map(int, input().split())
ls = sorted(list(map(int, input().split())))
cnt = 0

for i in range(n):
  if ls[i] >= x:
    cnt +=1

ans = cnt
s= 0
e = n - cnt -1
rest_cnt = n-cnt
while s < e:
  if ls[s] + ls[e] >= x/2:
    ans += 1
    s += 1
    e -= 1
    rest_cnt -= 2
  else :
    s+=1

ans += rest_cnt // 3
print(ans)