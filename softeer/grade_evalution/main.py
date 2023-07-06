import sys
import copy

def printRank(n, arr):
    temp_arr = copy.copy(arr)
    temp_arr.sort(reverse=True)
    dic = {}
    for i in range(n):
        if i != 0 and temp_arr[i-1] == temp_arr[i]:
            continue
        dic[temp_arr[i]] = i + 1
    
    for i in range(n):
        print(dic[arr[i]], end=" ")
    print()


def main():
    n = int(input())
    
    sum_arr = [0] * n

    for i in range(3):
        arr = list(map(int, input().split()))
        for j in range(n):
            sum_arr[j] += arr[j]
        printRank(n, arr)
    
    printRank(n, sum_arr)
    
    return

main()