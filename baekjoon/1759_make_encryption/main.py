from itertools import combinations

def solution():
    vowels = ('a', 'e', 'i', 'o', 'u') 
    n, m = list(map(int, input().split()))

    char_arr = input().split()
    char_arr.sort()
    com_list = combinations(char_arr, n)
    for res in com_list:
        vowel_cnt = 0
        for c in res:
            if c in vowels:
                vowel_cnt += 1
                
        if vowel_cnt >= 1 and vowel_cnt <= n - 2:
            print("".join(res))

solution()