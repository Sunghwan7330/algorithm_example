
def solution():
    n = int(input())
    m = int(input())

    res = []
    max_val = 9999999999
    for i in range(n):
        res.append([max_val] * n)
    for i in range(n):
        res[i][i] = 0
    

    buslist = []
    for _ in range(m):
        a, b, cost = map(int, input().split())
        a -= 1
        b -= 1
        res[a][b] = min(res[a][b], cost)
        buslist.append([a, b, cost])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])


    for i in range(n):
        for j in range(n):
            if res[i][j] == max_val:  print(0, end=" ")
            else : print(res[i][j], end=" ")
        print()

    return 

solution()
    
