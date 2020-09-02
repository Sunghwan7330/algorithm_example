def solution(n, lost, reserve):
    list = [1 for i in range(n)]

    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            list[i - 1] = 0

    for i in reserve:
        num = i - 2
        if num >= 0:
            if list[num] == 0:
                list[num] = 1
                continue

        num = i
        if num < n:
            if list[num] == 0:
                list[num] = 1
                continue

    answer = 0
    for i in list:
        if i == 1:
            answer += 1

    return answer

def main():
    testcases = [
        [5, [2, 4], [1, 3, 5], 5],
        [5, [2, 4], [3], 4],
        [3, [3], [1], 2]
    ]

    num = 1
    for tc in testcases:
        print("* %d." % num)
        if solution(tc[0], tc[1], tc[2]) == tc[3]:
            print("  - success")
        else:
            print("  - fail")
        num += 1


if __name__ == "__main__":
    main()
