import math

def solution(N):
    arr_len = len(N)
    peek_arr = []

    for i in range(1, arr_len - 1):
        if N[i-1] < N[i] > N[i+1]:
            peek_arr.append(i)

    peek_len = len(peek_arr)
    if peek_len <= 2:
        return peek_leni

    # 제일 처음 peak와 끝 peak 사이에 최대한 깃발을 꽂을 수 있는 갯수
    maxflag = int(math.sqrt(peek_arr[-1]-peek_arr[0]))+1
            
    # 제일처음 peak에서부터 조건을 비교하면서, count로 체크한 후 flag 수(f)를 return
    for f in range(maxflag, 2, -1):
        count = 1
        p = peek_arr[0]
        for i, pe in enumerate(peek_arr):
            if f <= pe-p:
                count += 1
                p = pe
                     
        if count >= f:
            break

    return f

def main():
    testcases = [
        [[1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2], 3]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0])
        print("  answer : " + str(ret))

        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
