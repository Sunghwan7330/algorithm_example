
def solution():
    n = int(input())

    path = []
    for i in range(n):
        path.append(list(map(int, input().split())))


    for k in range(n):
        for i in range(n):
            for j in range(n):
                if path[i][k] & path[k][j] != 0:
                    path[i][j] = 1

    for i in range(n):
        for j in range(n):
            print(path[i][j], end=" ")
        print()

    return 

solution()
    
