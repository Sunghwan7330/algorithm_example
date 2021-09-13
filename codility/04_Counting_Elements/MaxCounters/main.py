def solution(N, A):
    answer = [0 for i in range(N)]
    max_val = 0
    max_count = 0

    for n in A:
        if n == N+1:
            max_count = max_val

        else:
            if answer[n-1] < max_count: answer[n-1] = max_count
            answer[n-1] += 1
            if max_val < answer[n-1]:
                max_val = answer[n-1]
    for i in range(N):
        if answer[i] < max_count:
            answer[i] = max_count

    return answer


def main():
    testcases = [
        [5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2]]
    ]

    num = 1
    print("* %d." % num)
    for tc in testcases:
        ret = solution(tc[0], tc[1])
        res = True
        for i in range(len(tc[2])):
            if ret[i] != tc[2][i]:
                res = False
                break

        if res:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()