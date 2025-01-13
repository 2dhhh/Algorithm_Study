import sys

input = sys.stdin.readline

n = int(input())

# 문자열 입력
s = " "+input()

# 인덱스는 n+1 까지
E_suffix = [0] * (n+2)
W_prefix = [0] * (n+2)

for i in range(n+1)[::-1]:
  if s[i] == 'E':
    E_suffix[i] = E_suffix[i+1] + 1
  else:
    E_suffix[i] = E_suffix[i+1]

for i in range(1,n+1):
  if s[i] == 'W':
    W_prefix[i] = W_prefix[i-1] + 1
  else:
    W_prefix[i] = W_prefix[i-1]

ans = 0
for i in range(len(s)):
  if s[i] == 'H':
    ans += (W_prefix[i] * (pow(2,E_suffix[i]) - E_suffix[i] -1))

mod = 1_000_000_007
print(ans % mod)
