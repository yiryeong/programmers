from collections import defaultdict


def solution(phone_book):
    answer = True
    pd = defaultdict(list)

    for p in phone_book:
        pd[len(p)].append(p)

    pl = list(pd.items())

    for key1, value1_list in pl:
        for key2, value2_list in pl:
            if key2 > key1:
                value_dict = {}
                for value1 in value1_list:
                    if value1 in value_dict.keys():
                        return False
                    value_dict[value1] = 1

                for value2 in value2_list:
                    if value2[:key1] in value_dict.keys():
                        return False

    return answer
