def solution(X, Y, D):
    Y -= X
    res = divmod(Y, D)

    answer = res[0]

    if res[1] != 0:
        answer += 1
    return answer


def main():
    
    testcases = [
        [10, 85, 30, 3]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0], tc[1], tc[2])
        if ret == tc[3]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
