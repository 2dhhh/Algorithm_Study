from itertools import permutations

num = list(range(1,10)) # [1,2,3,4,..,9]

num_pool = []

for i in permutations(num,3 ):
  num_pool.append(i) # num_pool=[123, 124, .. , 987] 1~9로 조합한 모든 경우의 수

n = int(input())

for _ in range(n):
  checking, ans_ts, ans_tb = map(int, input().split())
  poss = []

  for num_check in num_pool:
    strike, ball = 0, 0
    for i, check in enumerate(str(checking)):
      if int(check) == num_check[i]:
        strike += 1

      if int(check) != num_check[i] and int(check) in num_check:
        ball += 1


    if strike == ans_ts and ball == ans_tb:
      poss.append(num_check)

  num_pool = poss

print(len(poss))



