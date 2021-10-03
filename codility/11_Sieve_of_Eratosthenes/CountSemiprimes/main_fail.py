def solution(N, P, Q):
    prime_check_arr = [True] * (N+1)
    semiprime_cache_arr = [-1] * (N+1)
    prime_list = []
    
    for i in range(2,N+1):
        if prime_check_arr[i]:
            prime_list.append(i)
            for j in range(2*i, N+1, i):
                prime_check_arr[j] = False

    #print(prime_list)

    answer = []
    for i in range(len(P)):
        start_idx = P[i]
        end_idx = Q[i]
        cnt = 0
        for j in range(start_idx, end_idx+1):
            if semiprime_cache_arr[j] != -1:
                cnt += semiprime_cache_arr[j]
                continue
            semiprime_check = False
            for p in prime_list:
                if j % p == 0 and (j // p) in prime_list:
                    semiprime_check = True
                    break

            if semiprime_check:
                cnt += 1
                semiprime_cache_arr[j] = 1
            else: 
                semiprime_cache_arr[j] = 0
        answer.append(cnt)

    return answer


def main():
    testcases = [
        [26, [1, 4, 16], [26, 10, 20], [10, 4, 0]]
    ]

    num = 1

    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0], tc[1], tc[2])
        print("  answer : " + str(ret))
        res = True
        for i in range(len(tc[3])):
            if ret[i] != tc[3][i]:
                res = False
                break

        if res:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()
