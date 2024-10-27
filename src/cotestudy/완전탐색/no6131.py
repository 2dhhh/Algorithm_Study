cnt = 0
n = int(input())

for i in range(1, 501):
    for j in range(1, i):
        if i*i - j*j == n:
            cnt += 1
print(cnt)
