from itertools import combinations

def input_city(city, n, homes, chicken):
    for i in range(n):
        in_row = input().split()
        row = []
        for j in range(n):
            v = int(in_row[j])
            row.append(v)

            if   v == 1:  homes.append([i, j])
            elif v == 2:  chicken.append([i, j])
        city.append(row)

def get_sum(homes, candidate):
    result = 0

    for hx, hy in homes:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result


def solution():
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])

    city = []
    homes = []
    chicken = []
    input_city(city, n, homes, chicken)

    candidates = list(combinations(chicken, m))
    
    result = 1e9
    for candidate in candidates:
        result = min(result, get_sum(homes, candidate))

    return result

print(solution())
