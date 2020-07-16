def convert_member_arr_to_dic(arr):
    dic = {}
    for mem in arr:
        if dic.get(mem) is None:
            dic[mem] = 1
        else:
            dic[mem] = dic[mem] + 1
    return dic


def solution(participant, completion):
    part_dic = convert_member_arr_to_dic(participant)
    comp_dic = convert_member_arr_to_dic(completion)

    for mem in part_dic:
        if comp_dic.get(mem) is None:
            return mem

        if part_dic[mem] != comp_dic[mem]:
            return mem

    answer = ''
    return answer


def main():
    testcases = [[["leo", "kiki", "eden"], ["eden", "kiki"], "leo"],
                 [["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"], "vinko"],
                 [["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"], "mislav"]]

    num = 1
    for tc in testcases:
        print("* %d." % num)
        if solution(tc[0], tc[1]) == tc[2]:
            print("  - success")
        else:
            print("  - fail")
        num += 1


if __name__ == "__main__":
    main()
