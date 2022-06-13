from collections import deque

def print_maze(maze):
    for m in maze:
        print(m)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution():
    n, m = map(int, input().split())

    maze = []
    for _ in range(n):
        maze.append(list(map(int, list(input()))))
        
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        cur_cnt = maze[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n : continue
            if ny < 0 or ny >= m : continue
            if maze[nx][ny] != 1 : continue

            maze[nx][ny] = cur_cnt + 1
            queue.append((nx, ny))

    print(maze[n-1][m-1])
    return 

solution()
