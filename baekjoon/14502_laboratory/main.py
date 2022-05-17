def get_score(lab):
    score = 0
    for r in lab:
        for c in r:
            if c == 0: score += 1
    
    return score


def print_lab(lab):
    for arr in lab:
        print(arr)


def spread_virus(lab, n, m):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = n + dx[i]
        ny = m + dy[i]

        if nx < 0 or nx >= len(lab): continue
        if ny < 0 or ny >= len(lab[nx]): continue
        if lab[nx][ny] == 0:
            lab[nx][ny] = 2
            spread_virus(lab, nx, ny)

    return


def get_virus_res(lab):
    temp_lab = []
    for v in lab:
        temp_lab.append(v[:])
    
    for i in range(len(temp_lab)):
        for j in range(len(temp_lab[i])):
            if temp_lab[i][j] == 2:
                spread_virus(temp_lab, i, j)
    
    return get_score(temp_lab)

res = 0
def add_fence_dfs(lab, count):
    if count == 3:
        global res
        res = max(res, get_virus_res(lab))
        return
    
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                add_fence_dfs(lab, count)
                count -= 1
                lab[i][j] = 0
    return res


def solution():
    n, m = map(int, input().split())

    lab = []
    for _ in range(n):
        lab.append(list(map(int, input().split())))

    print(add_fence_dfs(lab, 0))

    return 

solution()
