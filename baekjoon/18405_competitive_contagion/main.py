def print_testtube(testtube):
    for arr in testtube:
        print(arr)


def virus_wave(testtube, virus_arr):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(testtube)
    vir_len = len(virus_arr)

    for i in range(1, vir_len):
        arr = virus_arr[i]
        new_arr = []
        for x, y in arr:
            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]

                if nx < 0 or nx >= n: continue
                if ny < 0 or ny >= n: continue
                if testtube[nx][ny] != 0 : continue

                testtube[nx][ny] = i
                new_arr.append([nx, ny])
        virus_arr[i] = new_arr

    return


def solution():
    n, k = map(int, input().split())
    virus_arr = [[] * n for _ in range(k+1)]

    testtube = []
    for i in range(n):
        arr = list(map(int, input().split()))
        testtube.append(arr)
        for j in range(n):
            if testtube[i][j] != 0:
                virus_arr[testtube[i][j]].append([i, j])

    s, x, y = map(int, input().split())
    x -= 1
    y -= 1

    for i in range(s):
        virus_wave(testtube, virus_arr)
        #print_testtube(testtube)
        #print()
        if testtube[x][y] != 0:  break
        

    print(testtube[x][y])

    return 

solution()
