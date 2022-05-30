import heapq

def get_short_distance(mars):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = len(mars)

    dis_arr = []
    for i in range(n):
        dis_arr.append([999999999] * n)

    dis_arr[0][0] = mars[0][0]
    x, y = 0, 0
    q = [(mars[0][0], x, y)]
    while q:
        dis, x, y = heapq.heappop(q)

        if dis_arr[x][y] < dis: continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx < 0: continue
            if ny >= n or ny < 0: continue
            
            
            cost = dis + mars[nx][ny]
            if cost < dis_arr[nx][ny]:
                dis_arr[nx][ny] = cost
                heapq.heappush(q,(cost, nx, ny))

    """
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= n or nx < 0: continue
                if ny >= n or ny < 0: continue
                
                dis_arr[nx][ny] = min(dis_arr[nx][ny], dis_arr[x][y] + mars[nx][ny])
                
        #print(dis_arr)
    """
    return dis_arr[n-1][n-1]

def solution():
    t = int(input())

    for i in range(t):
        n = int(input())
        mars = []
        for _ in range(n):
            mars.append(list(map(int, input().split())))
        print(get_short_distance(mars))

    

    return

solution()
