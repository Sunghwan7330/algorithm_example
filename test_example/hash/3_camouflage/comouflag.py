def solution(clothes):
    cloth_dic = {}

    for cloth in clothes:
        if cloth_dic.get(cloth[1]) is None:
            cloth_dic[cloth[1]] = 1
        else:
            cloth_dic[cloth[1]] += 1

    case_cnt = 1
    for value in cloth_dic.values():
        case_cnt *= value + 1

    return case_cnt - 1


def main():
    test_cases = [
        [[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]], 5],
        [[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]], 3]
    ]

    num = 1
    for tc in test_cases:
        print("* %d." % num)
        if solution(tc[0]) == tc[1]:
            print("  - success")
        else:
            print("  - fail")
        num += 1


if __name__ == "__main__":
    main()
