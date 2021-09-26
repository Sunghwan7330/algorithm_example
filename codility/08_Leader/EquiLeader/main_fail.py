def solution(A):
    dic = {}
    front_dic = {}
    arr_len = len(A)
    arr_a = []
    for i in range(arr_len):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1

        domin_cnt = (i+1) // 2
        domin_val = -1
        check_val = 0;
        for key, value in dic.items():
            if value > domin_cnt:
                domin_val = key
                break
            check_val += value
            if check_val > domin_cnt:
                break
        arr_a.append(domin_val)
       
    dic = {}
    answer = 0
    for i in range(arr_len-1, 0, -1):
        if A[i] in dic:
            dic[A[i]] += 1
        else:
            dic[A[i]] = 1

        domin_cnt = (arr_len - i) // 2
        domin_val = -1
        check_val = 0;
        for key, value in dic.items():
            if value > domin_cnt:
                domin_val = key
                break
            check_val += value
            if check_val > domin_cnt:
                break

        if domin_val == -1:
            continue
        if arr_a[i-1] == domin_val:
            answer += 1
       
    return answer


def main():
    testcases = [
        [[4, 3, 4, 4, 4, 2], 2],
        [[1, 2, 3, 4, 5], 0]
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
