def get_distance(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2)

def solution():
    n = int(input())

    maparr = []
    for _ in range(n):
        maparr.append(list(map(int, input().split())))

    fish_arr = []
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if maparr[i][j] == 9:
                x = i
                y = j
                continue
            if maparr[i][j] != 0:
                fish_arr.append([maparr[i][j], i, j])

    time = 0
    shark_size = 2
    exp = 0
    while len(fish_arr) != 0:
        idx = -1
        cur_size = 9
        distance = 99999999999
        for i in range(len(fish_arr)):
            size, x2, y2 = fish_arr[i]
            if size >= shark_size: continue

            dis = get_distance(x, y, x2, y2)
            if dis < distance:
                idx = i
                distance = dis
                cur_size = size

        if idx == -1: break

        
        time += distance
       
        x = fish_arr[idx][1]
        y = fish_arr[idx][2]

        exp += 1
        if exp == shark_size:
            shark_size += 1
            exp = 0
        print(fish_arr[idx])
        print("size : %d, exp : %d, time : %d" % (shark_size, exp, time))
        fish_arr.pop(idx)

    print(fish_arr)    
    print(time)
    return


solution()
