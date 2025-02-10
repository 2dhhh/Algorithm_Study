import sys

input = sys.stdin.readline

g = int(input())

s = 1
e = 2
check = False

while e <= 100000:
  diff = e ** 2 - s ** 2
  if diff == g:
    print(e)
    check = True
    e += 1
  elif diff < g:
    e += 1
  else:
    s += 1

if not check:
  print(-1)