a, b, c, n = map(int, input().split())
ans = 0
flag = False
for i in range(0, 301):
    for j in range(0, 151):
        for k in range(0, 100):
            if a*i + b*j + c*k == n:
                ans = 1
                flag = True
                break
        if flag:
            break
    if flag:
        break
print(ans)