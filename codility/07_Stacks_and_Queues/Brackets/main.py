def solution(A):
    stack = []
    for c in A:
        if c == '[' or c == '{' or c == '(':
            stack.append(c)
        elif c == ']':
            if len(stack) == 0:
                return 0
            if stack.pop() != '[':
                return 0
        elif c == '}':
            if len(stack) == 0:
                return 0
            if stack.pop() != '{':
                return 0
        elif c == ')':
            if len(stack) == 0:
                return 0
            if stack.pop() != '(':
                return 0
    if len(stack) != 0:
        return 0

    return 1


def main():
    testcases = [
        ["{[()()]}", 1],
        ["([)()]", 0]
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
