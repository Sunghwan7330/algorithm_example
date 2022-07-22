
def solution():
    n = int(input())
    mem_list = list(map(int, input().split()))

    mem_list.sort()

    res = 0
    length = len(mem_list)
    for i in range(length):
        res += mem_list[i] * (length - i)

    print(res)
    return

solution()