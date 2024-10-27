n = int(input())
cnt = 0


for i in range (1, n-2):
    for j in range(1, n-2):
        k = n - i - j
        if i + j + k == n:
            if i % 2 == 0 and k >= j + 2:
                cnt += 1

print(cnt)
