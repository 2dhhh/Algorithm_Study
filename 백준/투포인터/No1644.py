import math
import sys

input = sys.stdin.readline

n = int(input())

ls = [True] * (n+1)

for i in range(2, int(math.sqrt(n))+ 1):
  if ls[i]:
    j = 2
    while i*j <= n:
      ls[i*j] = False
      j += 1

p_ls = []
for i in range(2,n+1):
  if ls[i]:
    p_ls.append(i)

r = -1
total = 0
cnt = 0
for l in range(len(p_ls)):
  while r + 1 < len(p_ls) and total < n:
    r += 1
    total += p_ls[r]

  if total == n:
    cnt += 1
  total -= p_ls[l]
print(cnt)