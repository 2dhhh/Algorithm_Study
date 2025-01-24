import sys

input = sys.stdin.readline

n = int(input())

hoof = [0] * (n+1)
scissors = [0] * (n+1)
paper = [0] * (n+1)

for i in range(1,n+1):
  str = input().rstrip()

  if str == 'H' :
    hoof[i] = hoof[i-1] +1
    scissors[i] = scissors[i-1]
    paper[i] = paper[i-1]
  elif str == 'S' :
    hoof[i] = hoof[i-1]
    scissors[i] = scissors[i-1] +1
    paper[i] = paper[i-1]

  else :
    hoof[i] = hoof[i-1]
    scissors[i] = scissors[i-1]
    paper[i] = paper[i-1] +1

ans = 0
for i in range(1, n+1):
  h_s = hoof[i-1] + (scissors[n] - scissors[i-1])
  h_p = hoof[i-1] + (paper[n] - paper[i-1])
  s_h = scissors[i-1] + (hoof[n] - hoof[i-1])
  s_p = scissors[i-1] + (paper[n] - paper[i-1])
  p_h = paper[i-1] + (hoof[n] - hoof[i-1])
  p_s = paper[i-1] + (scissors[n] - scissors[i-1])

  ans = max(h_s, h_p, s_h, s_p, p_h, p_s,ans)

print(ans)

