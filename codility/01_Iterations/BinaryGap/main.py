def solution(N):

    long_gap = 0
    gap_count = 0
    mask = 1
    count_flag = False

    while N > 0:
        if N & mask == 1:
            if gap_count > long_gap:
                long_gap = gap_count
            gap_count = 0
            count_flag = True
        else:
            if count_flag:
                gap_count += 1

        N = N >> 1
    return long_gap

def main():
    
    testcases = [
      [9, 2], [529, 4], [20, 1], [32, 0], [1041, 5], [32, 0]
    ]
 
    for tc in testcases:  
        ret = solution(tc[0])
        if ret == tc[1]:
            print("  - success")
        else:
            print("  - fail")
    

if __name__ == "__main__":
    main()
