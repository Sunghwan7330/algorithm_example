def solution(A):
    dic = {}
    arr_len = len(A)
    for i in range(arr_len):
        if A[i] in dic:
            dic[A[i]].append(i)
        else:
            dic[A[i]] = [i]

    divres = divmod(arr_len, 2)
    domin_val = divres[0]
    domin_val += 1

    for key, value in dic.items():
        if len(value) >= domin_val:
            return value[0]

    return -1


def main():
    testcases = [
        [[3, 4, 3, 2, 3, -1, 3, 3], [0, 2, 4, 6, 7]]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0])
        print("  answer : " + str(ret))
        res = False
        for i in range(len(tc[1])):
            if tc[1][i] == ret:
                res = True
                break
        if res:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
