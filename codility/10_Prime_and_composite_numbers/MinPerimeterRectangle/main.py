import math 

def solution(N):
    sqrt = int(math.sqrt(N))

    for i in range(sqrt, 0, -1):
        mod = N % i
        if mod == 0:
            n = N // i 
            return (i+n) * 2

    return 0

def main():
    testcases = [
        [30, 22],
        [1, 4],
        [2, 6]
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
