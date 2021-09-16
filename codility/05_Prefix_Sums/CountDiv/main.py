def solution(A, B, K):
    div_a = divmod(A, K)
    div_b = divmod(B, K)

    val_a = div_a[0]
    if div_a[1] == 0:
        val_a -= 1
    val_b = div_b[0]

    return val_b - val_a


def main():
    testcases = [
        [6, 11, 2, 3]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0], tc[1], tc[2])
        print("  answer : " + str(ret))

        if ret == tc[3]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
