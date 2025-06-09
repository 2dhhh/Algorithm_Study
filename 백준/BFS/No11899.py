from collections import deque

s = input()
q = deque()
ans = 0
for i in s:
  if i == '(':
    q.append(i)
  # i 가 ) 인 경우
  else:
    if q:
      q.pop()
    else:
      ans += 1
ans += len(q)
print(ans)