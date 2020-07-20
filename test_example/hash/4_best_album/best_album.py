
def solution(genres, plays):
    album_sum = {}
    album_attr = {}


    
    for i in range(0, len(genres)):
        if album_sum.get(genres[i]) is None:
            album_sum[genres[i]] = plays[i]
            album_attr[genres[i]] = [(i, genres[i], plays[i])]
        else:
            album_sum[genres[i]] += plays[i]
            album_attr[genres[i]].append((i, genres[i], plays[i]))

    for key in album_sum.keys():
        album_attr[key] = sorted(album_attr[key], key = lambda album: album[2], reverse=True)


    answer = []
    while len(album_sum) is not 0:
        max_play = -1
        max_key = ""

        for key in album_sum.keys():
            if max_play < album_sum[key]:
                max_play = album_sum[key]
                max_key = key
        
        answer.append(album_attr[key][0][0])
        if len(album_attr) >= 2:
            answer.append(album_attr[key][1][0])

        del(album_sum[max_key])

    return answer


def main():
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    res = [4, 1, 3, 0]


    if solution(genres, plays) == res:
        print("  - success")
    else:
        print("  - fail")


if __name__ == "__main__":
    main()
