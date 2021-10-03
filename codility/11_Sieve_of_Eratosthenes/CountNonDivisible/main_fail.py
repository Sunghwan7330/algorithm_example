def solution(A):
    arr_len = len(A)

    cnt_arr = [0] * ((arr_len*2) + 1)
    cache_arr = [-1] * ((arr_len*2) + 1)

    for n in A:
        cnt_arr[n] += 1
    
    answer = []
    for n in A:
        if cache_arr[n] != -1:
            answer.append(cache_arr[n])
            continue

        cnt = 0
        for i in range(1, n+1):
            if cnt_arr[i] == 0:
                continue
            if n % i == 0:
                cnt += cnt_arr[i]
        cnt = arr_len - cnt
        answer.append(cnt)
        cache_arr[n] = cnt

    return answer


def main():
    testcases = [
        [[3, 1, 2, 3, 6], [2, 4, 3, 2, 0]]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0])
        print("  answer : " + str(ret))
        res = True
        for i in range(len(tc[1])):
            if ret[i] != tc[1][i]:
                res = False
                break

        if res:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
