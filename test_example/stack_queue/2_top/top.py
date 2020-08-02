def solution(heights):
    answer = [0] * len(heights)

    top_len = len(heights)
    for i in range(0, top_len):
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break

    return answer

def main():
    testcases = [
        [[6,9,5,7,4], [0,0,2,2,4]],
        [[9,6,5,7,4], [0,1,2,1,4]],
        [[3,9,9,3,5,7,2], [0,0,0,3,3,3,6]],
        [[1,5,3,6,7,6,5], [0,0,2,0,0,5,6]]
    ]
    
    num = 1
    for tc in testcases:
        print("* %d." % num)
        if solution(tc[0]) == tc[1]:
            print("  - success")
        else:
            print("  - fail")
        num += 1


if __name__ == "__main__":
    main()
