import sys
input = sys.stdin.readline

a,b,n,w = map(int, input().split())
cnt = 0
sheep = 0
goat = 0

for i in range(1,n):
  if (a-b)*i + b*n == w:
    cnt += 1
    sheep = i
    goat = n-i

if cnt == 1 :
  print(sheep, goat)

else :
  print(-1)


