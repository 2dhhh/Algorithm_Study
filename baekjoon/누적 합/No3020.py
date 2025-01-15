import sys
input = sys.stdin.readline

n, h = map(int, input().split())
# 종유석
under = [0] * (h+1)
#석순
over = [0] * (h+1)

for i in range(n):

  if i % 2 == 0:
    over[int(input())] += 1
  else:
    under[h-int(input())+1] += 1

for i in range(h-1, 0, -1):
  over[i] += over[i+1]
for i in range(2, h+1):
  under[i] += under[i-1]

total = [0] * (h+1)
for i in range(1, h+1):
  total[i] = over[i] + under[i]

ans = total[1:]
val = min(ans)
print(val, ans.count(val))