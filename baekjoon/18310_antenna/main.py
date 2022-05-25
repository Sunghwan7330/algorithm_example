
def solution():
    n = int(input())
    pos_arr = list(map(int, input().split()))

    pos_arr.sort()

    a = int(n/2)
    a += n % 2
    a -= 1

    print(pos_arr[a])

solution()



