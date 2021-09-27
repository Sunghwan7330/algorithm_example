def solution(A):
    arr = A[1:-1]
    arr_len = len(arr)
    m = -100000

    if arr_len == 1:
        return 0

    c = 0
    start_idx = 0
    end_idx = 0
    tmp_idx = 0
    for i in range(arr_len):
        c = c + arr[i]

        if c < 0:
            c = 0
            tmp_idx = i+1
        else :
            if m < c:
                m = c
                start_idx = tmp_idx
                end_idx = i
    
    #print("%d - %d" %(start_idx, end_idx))
    #print(arr[start_idx:end_idx+1])
    """
    if start_idx >= arr_len:
        return 0
    """
    if m < 0:
        return 0
    if start_idx == end_idx : 
        return m
    min_val = min(arr[start_idx:end_idx+1])
    if min_val < 0:
        return m - min_val
    if start_idx == 0 and end_idx == arr_len-1:
        return m - min_val
    
    return m


def main():
    testcases = [
        [[3, 2, 6, -1, 4, 5, -1, 2], 17],
        [[0, 10, -5, -2, 0], 10],
        [[0, -1, 10, -5, -2, 0], 10],
        [[5, 5, 5], 0],
        [[-8, 10, 20, -5, -7, -4], 30],
        [[6, 1, 5, 6, 4, 2, 9, 4], 26],
        [[-2, -3, -4, 1, -5, -6, -7], 1],
        [[-4, -5, -1, -5, -7, -19, -11], 0]
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
