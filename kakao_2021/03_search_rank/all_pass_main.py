import bisect
from itertools import combinations

def solution(info, query_list):
    answer = []
    appl_info_arr = []
    alllicant_info_dic = {}

    for applicant_info in info:
        info_arr = applicant_info.split()
        info_key_arr = info_arr[:-1]
        info_val = int(info_arr[-1])

        for i in range(5):
            for c in combinations(info_key_arr, i):
                key = ''.join(c)
                #print(key)
                if key in alllicant_info_dic:
                    alllicant_info_dic[key].append(info_val)
                else:
                    alllicant_info_dic[key] = [info_val]

    for key, arr in alllicant_info_dic.items():
        arr.sort()

    #print(alllicant_info_dic)

    for q in query_list:
        q = q.split(" ")
        score = int(q[-1])
        q = q[:-1]
        
        for i in range(3):
            q.remove("and")
        while "-" in q:
            q.remove("-")
            
        key = ''.join(q)
        #print(key)

        if key in alllicant_info_dic:
            arr = alllicant_info_dic[key]
            all_len = len(arr)
            index = bisect.bisect_left(arr, score, lo=0, hi=all_len)
            answer.append(all_len - index)
        else:
            answer.append(0)
        
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
