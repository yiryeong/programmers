from collections import defaultdict


def solution(genres, plays):
    answer = []
    count_dict = defaultdict(int)
    song_dict = defaultdict(list)
    i = 0

    for g, p in zip(genres, plays):
        count_dict[g] += p
        song_dict[g].append((p, i))
        i += 1

    count_dict_sort = sorted(count_dict.items(), key=lambda x: -x[1])

    for key, count in count_dict_sort:
        song_list = sorted(song_dict[key], key=lambda x: (-x[0], x[1]))
        count = 0
        for s in song_list:
            if count > 1:
                break
            else:
                answer.append(s[1])
            count += 1

    return answer
