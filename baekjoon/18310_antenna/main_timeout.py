
def solution():
    n = int(input())
    pos_arr = list(map(int, input().split()))

    pos_arr.sort()

    min_pos = -1
    min_dis = 1000000

    for i in range(n):
        dis = 0
        for j in range(n):
            dis += abs(pos_arr[i] - pos_arr[j])
        
        if min_dis > dis:
            min_dis = dis
            min_pos = i
    print(pos_arr[min_pos])

solution()



