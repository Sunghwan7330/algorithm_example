def solution(X, A):
    arr_len = len(A)
    if X > arr_len:
        return -1

    check_arr = [0  for i in range(X)]
    leaf_len = 0

    for i in range(0, arr_len):
        if check_arr[A[i]-1] == 0:
            check_arr[A[i]-1] = 1
            leaf_len += 1
            if leaf_len == X:
                return i

    return -1


def main():
    
    testcases = [
        [5, [1, 3, 1, 4, 2, 3, 5, 4], 6]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0], tc[1])
        if ret == tc[2]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
