from itertools import permutations

def operation(a, b, oper):
    if oper == 0: return a + b
    elif oper == 1: return a - b
    elif oper == 2: return a * b
    elif oper == 3: return int(a / b)

    return


def solution():
    n = int(input())
    num = list(map(int, input().split()))
    oper_arr = list(map(int, input().split()))
    oper_list = []

    for i in range(4):
        for j in range(oper_arr[i]):
            oper_list.append(i)

    combi_res = permutations(oper_list, n-1)

    min_n = 1000000000
    max_n = -1000000000

    for combi_attr in combi_res:
        a = num[0]        
        for i in range(n-1):
            a = operation(a, num[i+1], combi_attr[i])
        min_n = min(a, min_n)
        max_n = max(a, max_n)

    print(max_n)
    print(min_n)

    return 

solution()
    
