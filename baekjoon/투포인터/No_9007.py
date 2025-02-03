import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  k, n = map(int, input().split())
  ls_12 = []
  ls_34 = []
  class1 = list(map(int, input().split()))
  class2 = list(map(int, input().split()))
  class3 = list(map(int, input().split()))
  class4 = list(map(int, input().split()))

  # 두 배열의 모든 조합 합 구하기
  for i in class1:
    for j in class2:
      ls_12.append(i + j)

  for i in class3:
    for j in class4:
      ls_34.append(i + j)


  ls_12.sort()
  ls_34.sort(reverse=True)

  ans = int(1e9)
  s, e = 0, 0

  while s < n * n and e < n * n:

    total = ls_12[s] + ls_34[e]

    # k에 더 가까운 값으로 갱신
    if abs(total - k) < abs(ans - k):
      ans = total

    elif abs(total - k) == abs(ans - k):
      ans = min(ans, total)  # 차이가 같다면 더 작은 값 선택

    if total < k:
      s += 1
    elif total > k:
      e += 1
    else:
      break  # 정확히 k일 경우 종료

  print(ans)