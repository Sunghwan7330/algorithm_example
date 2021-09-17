def solution(A):
    arr_len = len(A)
    sum_arr = [9000000000] * arr_len
    idx_arr = [-1] * arr_len

    for i in range(arr_len):
        sum_val = 0
        for j in range(arr_len - i):
            sum_val += A[i+j]
            if sum_arr[j] > sum_val:
                sum_arr[j] = sum_val
                idx_arr[j] = i

    min_aver = 1000000000
    idx = -1
    for i in range(1, arr_len):
        aver = sum_arr[i] / (i+1)
        if min_aver > aver:
            min_aver = aver
            idx = idx_arr[i]

    return idx


def main():
    testcases = [
        [[4, 2, 2, 5, 1, 5, 8], 1]
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
