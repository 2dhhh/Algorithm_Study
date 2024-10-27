intArray = list(map(int, input().split()))
for i in range(1, 1000000):
    cnt = 0
    for j in intArray:
        if i % j == 0:
            cnt += 1

    if cnt >= 3:
        print(i)
        break

