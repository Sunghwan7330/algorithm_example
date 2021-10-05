def solution(N, M):
    if M == 1 : return N
    if N == 1 : return 1

    a = N
    b = M
    while a != b:
        if a > b: a = a - b
        else : b = b - a
    return N // a

def main():
    testcases = [
        [10, 4, 5],
        [1000000000, 1, 1000000000],
        [1, 1000000000, 1]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0], tc[1])
        print("  answer : " + str(ret))

        if ret == tc[2]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
