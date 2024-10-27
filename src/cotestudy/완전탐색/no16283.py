a, b, n, w = map(int, input().split())
cnt = 0
sheep = 0
goat = 0
for x in range(1, n):
    if a*x + b*(n-x) == w:
        cnt += 1
        sheep = x
        goat = n-x

if cnt== 1 :
    print(sheep,goat)

else:
    print(-1)


