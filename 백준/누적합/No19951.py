import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 연병장 배열
ls = [0] + list(map(int, input().split()))
update_ls = [0] * (n+2)
prefix_sum = [0] * (n+2)

for i in range(m):
  a,b,k = map(int, input().split())
  update_ls[a] += k
  update_ls[b+1] += -k

for i in range(1,n+1):
  update_ls[i] += update_ls[i-1]
  ls[i] += update_ls[i]

for i in range(1, n+1):
  print(ls[i], end =" ")