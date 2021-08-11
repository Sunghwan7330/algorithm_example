info_dic = {
    "cpp" : 1,
    "java" : 2,
    "python" : 4,
    "backend" : 8,
    "frontend" : 16,
    "junior" : 32,
    "senior" : 64,
    "chicken" : 128,
    "pizza" : 256
}
DEV_LANG_LIST = [info_dic["cpp"], info_dic["java"], info_dic["python"]]
JOB_LIST = [info_dic["backend"], info_dic["frontend"]]
CAREER_LIST = [info_dic["junior"], info_dic["senior"]]
SOULFOOD_LIST = [info_dic["chicken"], info_dic["pizza"]]
LIST_ARR = [DEV_LANG_LIST, JOB_LIST, CAREER_LIST, SOULFOOD_LIST]
LIST_SUM_ARR = [sum(arr) for arr in LIST_ARR]


def convert_info_to_bit(info_arr):
    info_bit = 0
    for i in range(len(LIST_ARR)):
        if info_arr[i] == '-':
            info_bit += LIST_SUM_ARR[i]
        else:
            info_bit += info_dic[info_arr[i]]

    return info_bit


def decode_applicant_info(applicant_info):
    info_arr = applicant_info.split()
    info_bit = convert_info_to_bit(info_arr)

    return [info_bit, int(info_arr[-1])]

def solution(info, query_list):
    answer = []
    appl_info_arr = []

    for applicant_info in info:
        appl_info_arr.append(decode_applicant_info(applicant_info))
    #print(appl_info_arr)

    for query in query_list:
        query = query.replace(" and ", " ")
        items = query.split(" ")
        bit_val = convert_info_to_bit(items)
        score = int(items[-1])

        #print(query)
        #print(bit_val, score)

        total = 0
        for appl_info in appl_info_arr:
            if appl_info[0] & bit_val == appl_info[0] and  appl_info[1] >= score:
                total += 1
        answer.append(total)

    #print(answer)
    return answer

def main():
    testcases = [
        ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"],
        [1, 1, 1, 1, 2, 4]
    ]

    num = 1
    print("* %d." % num)
    ret = solution(testcases[0],testcases[1])
    res = 1
    for i in range(len(testcases[2])):
        if not ret[i] == testcases[2][i]:
            res = 0
            break
    if res == 1:
        print("  - success")
    else:
        print("  - fail")
    num += 1

if __name__ == '__main__':
    main()