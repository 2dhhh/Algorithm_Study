import sys

input = sys.stdin.readline

def check(a, b, operand):
  if operand == '<':
    if a > b:
      return False
  if operand == '>':
    if a < b:
      return False
  return True


def rec(k, ans):
  if k == n + 1:
    selected.append(ans)
    return
  for i in range(10):
    if visited[i]:
      continue
    if k == 0 or check(ans[k - 1], str(i), op[k - 1]):
      visited[i] = True
      rec(k + 1, ans + str(i))
      visited[i] = False


selected = []
visited = [False] * 10
n = int(input())
op = list(input().split())

rec(0, '')
selected.sort()
print(selected[-1])
print(selected[0])