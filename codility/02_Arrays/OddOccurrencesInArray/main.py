def solution(A):
    answer = 0
    for n in A:
        answer ^= n

    return answer


def main():
    
    testcases = [
        [[9, 3, 9, 3, 9, 7, 9], 7]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0])
        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
