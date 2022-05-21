def print_name(score_list):
    for a in score_list:
        print(a[0])
    return


def solution():
    n = int(input())
    score_list = []
    for i in range(n):
        score = input().split()
        score_list.append(score)

    score_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    print_name(score_list)
    return 

solution()
    
