a, b = list(map(int, input().split()))

arr = [0] * (b + 1)

arr[1] = 1
for i in range(2, b+1):
    if arr[i] == 0:
        n = i + i
        while n < b+1:
            arr[n] = 1
            n += i

for i in range(a, b+1):
    if arr[i] == 0:
        print(i)