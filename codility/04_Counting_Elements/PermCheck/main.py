def solution(A):
    arr_len = len(A)
    check_arr = [0 for i in range(arr_len)]
    for n in A:
        if n > arr_len:
            return 0
        check_arr[n-1] = 1

    for i in range(arr_len):
        if check_arr[i] == 0:
            return 0
    return 1


def main():
    
    testcases = [
        [[4, 1, 2, 3], 1],
        [[4, 1, 3], 0]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0])
        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
