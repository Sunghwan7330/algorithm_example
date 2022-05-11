
def dfs_road(road_dic, chk_arr, k, now_pos, depth):
    if chk_arr[now_pos][1] > depth:
        chk_arr[now_pos][1] = depth
    
    if depth == k:  return

    next_road_arr = road_dic[now_pos]


    for road in next_road_arr:
        if chk_arr[road][0] != 0 : continue
        
        chk_arr[road][0] = 1
        dfs_road(road_dic, chk_arr, k, road, depth+1)
        chk_arr[road][0] = 0
        
    return


def solution():
    input_val = input().split()
    n = int(input_val[0])
    m = int(input_val[1])
    k = int(input_val[2])
    x = int(input_val[3])

    road_dic = {}
    for i in range(m+2):
        road_dic[i] = []

    for i in range(m):
        input_road = list(map(int, input().split())) 
        road_dic[input_road[0]].append(input_road[1])

    check_arr = []
    for i in range(n+1):  check_arr.append([0, 10000000])

    check_arr[x][0] = 1
    dfs_road(road_dic, check_arr, k, x, 0)
     
    answer_flag = False
    for i in range(len(check_arr)):
        v = check_arr[i]
        if v[1] ==  k:
            print(i)
            answer_flag = True

    if answer_flag == False:  print(-1)
    
    return 

solution()
    
