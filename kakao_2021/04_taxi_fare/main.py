def print_distance(distance):
    for arr in distance:
        print(arr)
    return


def solution(n, s, a, b, fares):
    answer = 100000000
    dis = [ [100000000] * n for _ in range(n) ]

    for dis_info in fares:
        dis[dis_info[0] - 1][dis_info[1] - 1] = dis_info[2]
        dis[dis_info[1] - 1][dis_info[0] - 1] = dis_info[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]

    s -= 1
    a -= 1
    b -= 1
    for i in range(i):
        fare = dis[i][s] + dis[i][a] + dis[i][b]
        if fare < answer:
            answer = fare

    fare = dis[s][a] + dis[s][b]
    if fare < answer:
        answer = fare

    fare = dis[s][a] + dis[a][b]
    if fare < answer:
        answer = fare

    charge = dis[s][b] + dis[b][a]
    if charge < answer:
        answer = charge

    #print_distance(dis)
    #print(answer)
    return answer

def main():
    testcases = [
        [6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], 82],
        [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]], 14],
        [6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]], 18]
    ]

    num = 1
    print("* %d." % num)
    for tc in testcases:
        ret = solution(tc[0], tc[1], tc[2], tc[3], tc[4])
        if ret == tc[5]:
            print("  - success")
        else:
            print("  - fail")
        num += 1

if __name__ == '__main__':
    main()