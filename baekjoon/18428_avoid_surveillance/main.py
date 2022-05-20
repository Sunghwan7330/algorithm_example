def print_corridor(corridor):
    for arr in corridor:
        print(arr)

def is_surveillance(corridor, teacher_arr):
    n = len(corridor)
    for x, y in teacher_arr:
        for i in range(x, -1, -1):
            if corridor[i][y] == "O": break
            elif corridor[i][y] == "S": return False
        for i in range(x+1, n):
            if corridor[i][y] == "O": break
            elif corridor[i][y] == "S": return False

        for i in range(y, -1, -1):
            if corridor[x][i] == "O": break
            elif corridor[x][i] == "S": return False
        for i in range(y+1, n):
            if corridor[x][i] == "O": break
            elif corridor[x][i] == "S": return False

    return True


def dfs_setup_obj(corridor, teacher_arr, count):
    if count == 3:
        return is_surveillance(corridor, teacher_arr)
    
    n = len(corridor)
    for i in range(0, n):
        for j in range(0, n):
            if corridor[i][j] != "X": continue

            count += 1
            corridor[i][j] = "O"
            if dfs_setup_obj(corridor, teacher_arr, count) == True: return True
            corridor[i][j] = "X"
            count -= 1

    return False


def solution():
    n = int(input())

    corridor = []
    teacher_arr = []
    student_arr = []
    for i in range(n):
        arr = input().split()
        corridor.append(arr)
        for j in range(n):
            if corridor[i][j] == "T": teacher_arr.append([i, j])
            elif corridor[i][j] == "S": student_arr.append([i, j])

    if dfs_setup_obj(corridor, teacher_arr, 0): print("YES")
    else: print("NO")
    return 

solution()
