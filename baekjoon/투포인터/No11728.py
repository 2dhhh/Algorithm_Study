import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls_a = list(map(int, input().split()))
ls_b = list(map(int, input().split()))

ls = []

for i in range(n):
  ls.append(ls_a[i])

for i in range(m):
  ls.append(ls_b[i])

ls.sort()
print(*ls)