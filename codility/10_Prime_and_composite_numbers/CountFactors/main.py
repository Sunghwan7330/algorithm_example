import math 

def solution(N):
    if N == 1 or N == 2:
        return N

    cnt = 0  
    sqrt = int(math.sqrt(N))

    for i in range(1, sqrt+1):
        mod = N % i
        if mod == 0:
            cnt += 1
            
    cnt = cnt * 2
    if sqrt ** 2 == N :
        cnt -= 1

    return cnt

def main():
    testcases = [
        [24, 8],
        [16, 5]
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
