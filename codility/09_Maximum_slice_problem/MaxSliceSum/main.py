def solution(A):
    slice_sum = 0
    m = float('-inf')
    n = float('-inf')

    c = 0
    for a in A:
        c = c + a

        if n < a:
            n = a

        if c < 0:
            c = 0
        else :
            if m < c:
                m = c

    return m if 0 < m else n

def main():
    testcases = [
        [[3, 2, -5, 4, 0], 5]
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
