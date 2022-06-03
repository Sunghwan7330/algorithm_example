def solution():
    n, m = map(int, input().split())

    max_val = 9999999999
    floyd_arr = [[max_val] * n for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        floyd_arr[a][b] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                floyd_arr[i][j] = min(floyd_arr[i][j], floyd_arr[i][k] + floyd_arr[k][j])

    result = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if floyd_arr[i][j] < max_val or floyd_arr[j][i] < max_val:
                cnt += 1
        if cnt == n-1:
            result += 1

    print(result)
    return

solution()