import sys

input = sys.stdin.readline

# 입력
N,M,K = map(int, input().split())
ans = 0


# i는 여자 쪽 빼는 인원
for i in range(K+1):
  tmp = min((N-i)//2,M-(K-i))
  ans = max(ans, tmp)

print(ans)

