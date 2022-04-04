from collections import deque


def solution(numbers, target):
    answer = 0
    stack = deque([(0, numbers)])

    while stack:
        sum_value, number_list = stack.pop()

        if not number_list:
            if sum_value == target:
                answer += 1
        else:
            value = number_list[0]
            stack.append((sum_value - value, number_list[1:]))
            stack.append((sum_value + value, number_list[1:]))

    return answer
