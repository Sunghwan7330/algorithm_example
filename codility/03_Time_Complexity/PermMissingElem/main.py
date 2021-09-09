def solution(A):
    arrlen = len(A)
    check_arr = [0 for i in range(arrlen+1)]

    for n in A:
        check_arr[n-1] = 1

    for i in range(arrlen+1):
        if check_arr[i] is 0:
            return i+1

    return 0


def main():
    
    testcases = [
        [[2, 3, 1, 5], 4]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0])
        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
