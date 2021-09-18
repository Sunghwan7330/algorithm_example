def solution(A):
    arr_len = len(A)
    east_idx = []
    east_cnt = 0

    for i in range(arr_len):
        if A[i] == 0:
            east_idx.append(i)
            east_cnt += 1

    answer = 0
    for i in range(len(east_idx)):
        answer += arr_len - east_idx[i] - east_cnt
        east_cnt -= 1

    if answer > 1000000000:
        return -1

    return answer


def main():
    testcases = [
        [[0, 1, 0, 1, 1], 5],
        [[0, 1, 0, 1, 1, 0], 5],
        [[0], 0],
        [[1], 0]
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
