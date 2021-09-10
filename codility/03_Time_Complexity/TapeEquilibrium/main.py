def solution(A):
    min_val = 9999
    p1 = 0
    p2 = sum(A)
    for i in range(len(A)-1):
        p1 += A[i]
        p2 -= A[i]
        res = abs(p2 - p1)
        if min_val > res:
            min_val = res
        
    return min_val


def main():
    
    testcases = [
        [[3, 1, 2, 4, 3], 1]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0])
        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
