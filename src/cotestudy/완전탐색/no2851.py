intArray = [0] * 10
for i in range(10):
    intArray[i] = int(input())

sum = 0
ans = 100
for i in intArray:
    sum += i
    distance = abs(sum - 100)
    if(ans >= distance):
        ans = distance
    else:
        sum -= i
        break
print(sum)



