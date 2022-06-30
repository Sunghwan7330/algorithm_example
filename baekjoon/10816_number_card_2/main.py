
def solution():
    n = int(input())
    num_list = list(map(int, input().split()))

    num_dic = {}
    for num in num_list:
        if num in num_dic:
            num_dic[num] += 1
        else:
            num_dic[num] = 1
    #print(num_dic)

    m = int(input())
    num_list2 = list(map(int, input().split()))

    for num in num_list2:
        if num in num_dic:
            result = num_dic[num]
        else:
            result = 0
        print(result, end=" ")
    
solution()
