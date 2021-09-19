def solution(A):
    distinct_dic = {};

    for n in A:
        if n not in distinct_dic:
            distinct_dic[n] = n

    return len(distinct_dic)


def main():
    testcases = [
        [[2, 1, 1, 2, 3, 1], 3]
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
