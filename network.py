from collections import defaultdict


def solution(n, computers):
    answer = 0
    computers_dict = defaultdict(list)
    visited = [0] * n

    for i, value1 in enumerate(computers):
        for j, value2 in enumerate(value1):
            if value2 == 1 and i != j:
                computers_dict[i].append(j)

    for x in range(n):
        if visited[x] == 0:
            stack = [x]
            answer += 1

        while stack:
            node = stack.pop()

            if visited[node] == 0:
                visited[node] = 1
                stack.extend(computers_dict[node])

    return answer
