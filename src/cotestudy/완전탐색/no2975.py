n,m,k = map(int, input().split())
maxTeam = 0

for i in range(0, k+1):
    for j in range(0, k+1):
        if i + j == k:
            makeTeam = min((n-i)//2, m-j)
            if makeTeam > maxTeam:
                maxTeam = makeTeam
print(maxTeam)

