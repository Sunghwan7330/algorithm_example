
def get_min_coin_cnt(money, coin_list):
    res = 0
    length = len(coin_list)

    for i in range(length-1, -1, -1):
        q, r = divmod(money, coin_list[i])
        res += q
        money = r
        if money == 0:
            return res

    return res

def solution():
    n, money = map(int, input().split())

    coin_list = []
    for _ in range(n):
        coin_list.append(int(input()))
    
    print(get_min_coin_cnt(money, coin_list))

    return

solution()