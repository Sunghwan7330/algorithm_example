def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b);

def solution(A, B):
    tc_len = len(A)
    cnt = 0

    for i in range(tc_len):
        if A[i] == B[i]:
            cnt += 1
            continue
        if A[i] == 1 or B[i] == 1:
            continue

        gcd_val = gcd(B[i], A[i])

        gcd_a = 0
        gcd_b = 0

        a = A[i]
        b = B[i]

        while gcd_a != 1:
            gcd_a = gcd(a, gcd_val)
            a = a // gcd_a

        while gcd_b != 1:
            gcd_b = gcd(b, gcd_val)
            b = b // gcd_b

        if a == 1 and b == 1: 
            cnt += 1

    return cnt


def main():
    testcases = [
        [[15, 10, 3], [75, 30, 5], 1],
        [[6], [72], 1]
        
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
