from collections import deque

def mov_knight(n, pos, fin):
    dx = [2, 2, 1, -1, -2, -2, 1, -1]
    dy = [1, -1, 2, 2, 1, -1, -2, -2]
    chessmap = [[0] * n for _ in range(n)]

    queue = deque()
    queue.append(pos)
    x, y = pos
    cnt = 0
    chessmap[0][0] = cnt
    while queue:
        x, y = queue.popleft()
        cnt = chessmap[x][y]


        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n: continue
            if ny < 0 or ny >= n: continue
            #if chessmap[nx][ny] < cnt: continue
            if chessmap[nx][ny] != 0: continue

            queue.append((nx, ny))
            chessmap[nx][ny] = cnt + 1

    print(chessmap[fin[0]][fin[1]])

    return


def solution():
    cnt = int(input())
    for _ in range(cnt):
        n = int(input())
        pos = list(map(int, input().split()))
        fin = list(map(int, input().split()))
        if pos == fin : 
            print(0)
        else :
            mov_knight(n, pos, fin)


solution()
    
