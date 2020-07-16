def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(0, len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False

    return answer


def main():
    testcases = [[["119", "97674223", "1195524421"], False],
                 [["123", "456", "789"], True, ],
                 [["12", "123", "1235", "567", "88"], False]]

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
