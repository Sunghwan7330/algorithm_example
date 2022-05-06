def solution(val):
    input_len = len(val)
    half = int(input_len / 2)
    
    a = 0
    b = 0

    for i in range(half):
        a = a + int(val[i])
        b = b + int(val[-1-i])

    if a == b:
        return "LUCKY"

    return "READY"

def input_test():
    val = input()
    print(solution(val))

def auto_test():
    tc = [
        ["123402", "LUCKY"],
        ["7755", "READY"],
        ["1234321", "LUCKY"]
    ]

    for i in range(len(tc)):
        res = solution(tc[i][0])
        print("TC {} : ".format(i))
        print("input : {}".format(tc[i][0]))
        print("output : {}".format(tc[i][1]))
        if res == tc[i][1]: print("PASS!")
        else: print("FAIL!")
        print()

input_test()
#auto_test()
