import sys

input = sys.stdin.readline

N = int(input())
x_arr = []
y_arr = []

distance = 0

for i in range(N):
  x,y = map(int, input().split())
  x_arr.append(x)
  y_arr.append(y)

x_arr.sort()
y_arr.sort()

x_point = x_arr[N//2]
y_point = y_arr[N//2]

for i in range(N):
  distance += abs(x_point - x_arr[i]) + abs(y_point - y_arr[i])

print(distance)
