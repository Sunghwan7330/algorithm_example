def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="")
        print()


def get_next_pos(pos, direction):
    if direction == 0:  # 우
        pos[1] = pos[1] + 1
    elif direction == 1: # 하
        pos[0] = pos[0] + 1
    elif direction == 2: # 좌
        pos[1] = pos[1] - 1
    elif direction == 3: # 상
        pos[0] = pos[0] - 1


def check_gameover(board, snake_body, pos):
    x = pos[0]
    y = pos[1]
    n = len(board)

    if x < 0 or x > n-1:
        return True
    if y < 0 or y > n-1:
        return True
        
    for s_pos in snake_body:
        if s_pos[0] == pos[0] and s_pos[1] == pos[1]:
            return True

    return False


def solution():
    n = int(input())
    apple_cnt = int(input())

    board = [[0]*n for _ in range(n)]

    for i in range(apple_cnt):
        input_val = input().split()
        a = int(input_val[0]) - 1
        b = int(input_val[1]) - 1
    
        board[a][b] = 1

    direction_cnt = int(input())

    direction_arr = []
    for i in range(direction_cnt):
        input_val = input().split()
        a = int(input_val[0])
        b = input_val[1]
        direction_arr.append([a, b])

    #print_board(board, n)

    time = 0
    direction = 0
    pos = [0, 0]
    board[0][0] = 2
    snake_body = [[0, 0]]
    while True:
        time = time + 1
        
        get_next_pos(pos, direction)
        if check_gameover(board, snake_body, pos):
            return time;

        # 1. add body len
        snake_body.append([pos[0], pos[1]])

        # 2. check apple
        if board[pos[0]][pos[1]] == 1:
            board[pos[0]][pos[1]] = 0
        else: #3. delete snake tail
            snake_body.pop(0)
        if len(direction_arr) != 0:
            dir_val = direction_arr[0]
            if time == dir_val[0]:
                if dir_val[1] == 'D':
                    direction = (direction + 1) % 4
                elif dir_val[1] == 'L':
                    direction = (direction - 1) % 4
                direction_arr.pop(0)

print(solution())
    
