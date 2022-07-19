
def solution():
    c = int(input())
    parent_arr = [-1] * c
    node_arr = []
    for i in range(c):
        node_arr.append([])

    for i in range(c-1):
        a, b = map(int, input().split())
        node_arr[a-1].append(b-1)
        node_arr[b-1].append(a-1)

    print(node_arr)
    check_arr = [0] * c
    
    nstack = []
    nstack.append(0)
    check_arr[0] = 1
    while len(nstack) != 0:
        n = nstack.pop()
        for i in node_arr[n]:
            if check_arr[i] == 1:
                continue
            nstack.append(i)
            parent_arr[i] = n
            check_arr[i] = 1

    
    for i in range(1, len(parent_arr)):
        
        print(parent_arr[i] + 1)
    return 

solution()
    
