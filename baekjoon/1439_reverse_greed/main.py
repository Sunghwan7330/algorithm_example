def solution(val):
    cnt_arr = [0, 0]
    state = -1

    for i in range(len(val)):
        n = int(val[i])
        if state != n:
            state = n
            cnt_arr[n] = cnt_arr[n] + 1

    return min(cnt_arr[0], cnt_arr[1])

def input_test():
    val = input()
    solution(val)

def auto_test():
    tc = [
        ["0001100", 1],
        ["11111", 0],
        ["0000001", 1],
        ["11001100110011000001", 4],
        ["11101101", 2]
    ]

    for i in range(len(tc)):
        res = solution(tc[i][0])
        print("TC 1 : ")
        print("input : {}".format(tc[i][0]))
        print("output : {}".format(tc[i][1]))
        if res == tc[i][1]: print("PASS!")
        else: print("FAIL!")
        print()

#input_test()
auto_test()
