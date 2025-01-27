import sys

input = sys.stdin.readline

n = int(input())
ls = sorted(map(int, input().split()))

ans = int(1e10)
flags = False

for i in range(n-3):
  for j in range(i+3, n):
    s = i + 1
    e = j - 1
    while s < e:
      ans = min(ans, abs(ls[i] + ls[j] - (ls[s] + ls[e])))

      if ans == 0 :
        flags = True
        break
      if ls[i] + ls[j] < ls[s] + ls[e]:
        e -= 1

      else :
        s += 1

print(ans)
