from collections import deque, defaultdict


def check(a, b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
    return True if result == 1 else False


def solution(begin, target, words):
    answer = 0
    words_dict = defaultdict(list)
    visited = []
    stack = deque([(begin, 0)])

    if target in words:
        words.append(begin)
        for i, a in enumerate(words):
            for j, b in enumerate(words[i + 1:]):
                if check(a, b):
                    words_dict[a].append(b)
                    words_dict[b].append(a)

        while stack:
            node, count = stack.popleft()
            visited.append(node)

            if node == target:
                answer = count
                break

            for next_node in words_dict[node]:
                if next_node not in visited:
                    stack.append((next_node, count + 1))

    return answer
