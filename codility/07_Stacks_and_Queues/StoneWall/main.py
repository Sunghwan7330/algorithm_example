def solution(A):
    arr_len = len(A)
    stack = []
    cnt = 0
    for n in A:
        if len(stack) == 0:
            cnt += 1
            stack.append(n)
            continue

        if stack[-1] == n:
            continue
        
        if stack[-1] < n:
            stack.append(n)
            continue
           
        while len(stack) != 0 and stack[-1] > n:
            stack.pop()
            cnt += 1
        if len(stack) != 0 and stack[-1] == n:
            continue

        stack.append(n)
        continue
    while len(stack) > 1:
        stack.pop()
        cnt += 1
    return cnt


def main():
    testcases = [
        [[8, 8, 5, 7, 9, 8, 7, 4, 8], 7],
        [[2, 5, 1, 4, 6, 7, 9, 10, 1], 8]
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
