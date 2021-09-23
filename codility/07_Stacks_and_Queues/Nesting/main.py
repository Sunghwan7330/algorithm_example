def solution(A):
    stack = []
    for c in A:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return 0
            stack.pop()

    if len(stack) != 0:
        return 0

    return 1


def main():
    testcases = [
        ["(()(())())", 1],
        ["())", 0]
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
