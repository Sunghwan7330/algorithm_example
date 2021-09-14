def solution(A):
    check_arr = [0 for i in range(1000000)]

    for n in A:
        if n <= 0:
            continue
        check_arr[n-1] = 1

    for i in range(1000000):
        if check_arr[i] == 0:
            return i+1

    return 1000001


def main():
    testcases = [
        [[1, 3, 100000, 4, 1, 2], 5],
        [[1, 2, 3], 4],
        [[-1, -3], 1]
    ]

    num = 1
    print("* %d." % num)
    for tc in testcases:
        ret = solution(tc[0])

        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()