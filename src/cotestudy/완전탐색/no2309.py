intArray = [0] * 9
sum = 0

for i in range(0,9):
    intArray[i] = int(input())
    sum += intArray[i]

intArray.sort()
ans = sum - 100
idx1 = 0
idx2 = 0
for i in range(0,9):
    for j in range(1,9):
        if intArray[i] + intArray[j] == ans:
            idx1 = i
            idx2 = j

for i in range(0,9):
    if i == idx1 or i == idx2:
        continue
    else:
        print(intArray[i])

