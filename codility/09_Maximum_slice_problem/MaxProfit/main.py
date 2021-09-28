def solution(A):
    arr_len = len(A)
    slice_sum = 0
    m = float('-inf')

    c = 0
    for i in range(arr_len-1):
        diff = A[i+1] - A[i]
        c = c + diff

        if c < 0:
            c = 0
        else :
            if m < c:
                m = c

    return m if 0 < m else 0

def main():
    testcases = [
        [[23171, 21011, 21123, 21366, 21013, 21367], 356]
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
