
check_arr = []
course_dic = {}
def search_dfs(order, course, depth, size):
    if depth > size : return

    #print (course)

    global course_dic
    if len(course) >= 2:
        if not course in course_dic:
            course_dic[course] = 1
        else:
            course_dic[course] += 1

    global check_arr
    for i in range(0, size):
        if check_arr[i] == 0 :
            if course == '' or order[i] > course[-1]:
                check_arr[i] = 1
                next_course = course + order[i]
                search_dfs(order, next_course, depth+1, size)
                check_arr[i] = 0
    return

def process_course(order):
    size = len(order)

    global check_arr
    check_arr = [0 for i in range(size)]

    search_dfs(order, '', 0, size)

    return

def solution(orders, course):
    answer = []

    global course_dic
    course_dic = {}

    for order in orders:
        process_course(order)

    max_cource_arr = [0 for i in range(11)]
    for key, value in course_dic.items():
        if value >= 2:
            key_len = len(key)
            if key_len in course and max_cource_arr[key_len] < value:
                max_cource_arr[key_len] = value

    for key, value in course_dic.items():
        if value >= 2:
            key_len = len(key)
            if value == max_cource_arr[key_len]:
                answer.append(key)

    answer.sort()
    #print(answer)
    return answer

def main():
    testcases = [
        [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4], ["AC", "ACDE", "BCFG", "CDE"]],
        [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5], ["ACD", "AD", "ADE", "CD", "XYZ"]],
        [["XYZ", "XWY", "WXA"], [2, 3, 4], ["WX", "XY"]]
    ]

    num = 1
    for tc in testcases:
        print("* %d." % num)
        ret = solution(tc[0],tc[1])
        res = 1
        for i in range(len(tc[2])):
            if not ret[i] == tc[2][i]:
                res = 0
                break;
        if res == 1:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()