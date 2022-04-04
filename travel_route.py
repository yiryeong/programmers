from collections import defaultdict
import copy


def solution(tickets):
    answer = []
    tickets_dict = defaultdict(list)
    for start, to in tickets:
        tickets_dict[start].append(to)

    stack = [('ICN', tickets_dict, [])]

    while stack:
        node, d, history = stack.pop()
        history_new = history[::]
        history_new.append(node)

        if len(history_new) == len(tickets) + 1:
            answer.append(history_new)

        for next_node in d[node]:
            d_new = copy.deepcopy(d)
            d_new[node].remove(next_node)
            stack.append((next_node, d_new, history_new))

    return sorted(answer)[0]
