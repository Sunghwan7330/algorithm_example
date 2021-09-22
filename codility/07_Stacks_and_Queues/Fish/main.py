def solution(A, B):
    river = []
    arr_len = len(A)

    river.append([A[0], B[0]])
    for i in range(1, arr_len):
        tail = river[-1]
        if tail[1] == B[i]:
            river.append([A[i], B[i]])
            continue
        
        if tail[1] == 0 and B[i] == 1:
            river.append([A[i], B[i]])
            continue

        while True:
            if tail[0] > A[i]:
                break;

            if tail[0] < A[i]:
                river.pop()
            if len(river) == 0:
                river.append([A[i], B[i]])
                break;

            tail = river[-1]
            if tail[1] == B[i]:
                river.append([A[i], B[i]])
                break;

    return len(river)


def main():
    testcases = [
        [[4, 3, 2, 1, 5], [0, 1, 0, 0, 0], 2]
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
