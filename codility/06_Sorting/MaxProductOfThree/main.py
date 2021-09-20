def solution(A):
    A.sort()
    arr_len = len(A)

    max_val = A[arr_len-1] * A[arr_len-2] * A[arr_len-3]

    if A[0] < 0 and A[1] < 0:
        temp = A[0] * A[1] * A[arr_len-1]
        if temp > max_val:
            return temp

    return max_val


def main():
    testcases = [
        [[-3, 1, 2, -2, 5, 6], 60]
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
