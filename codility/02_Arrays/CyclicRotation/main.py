def solution(A, K):
    arr_len = len(A)
    if arr_len == 0:
        return A
    rot = K % arr_len

    if rot == 0:
        return A

    answer = A[-rot:] + A[0:(arr_len-rot)]
    return answer

def main():
    
    testcases = [
        [[3, 8, 9, 7, 6], 1, [6, 3, 8, 9, 7]],
        [[3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]],
        [[0, 0, 0], 3, [0, 0, 0]],
        [[1, 2, 3, 4], 4, [1, 2, 3, 4]]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0], tc[1])
        answ = True
        for i in range(len(ret)):
            if ret[i] != tc[2][i]:
                answ = False
                break
        if answ:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
