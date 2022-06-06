from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def cover_worm(field, x, y):

    n = len(field)
    m = len(field[0])
    
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if field[x][y] == 0:
            continue
        field[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= m: continue
            queue.append((nx, ny))

def earthworm():
    n, m, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]

    cabbage_arr = []
    for _ in range(k):
        a, b = map(int, input().split())
        cabbage_arr.append((a, b))
        field[a][b] = 1
    
    cnt = 0
    for x, y in cabbage_arr:
        if field[x][y] == 0:
            continue
        cover_worm(field, x, y)
        cnt += 1
    

    return cnt

def solution():
    c = int(input())
    for i in range(c):
        print(earthworm())

    return 

solution()
    
