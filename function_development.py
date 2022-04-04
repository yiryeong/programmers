import math


def solution(progresses, speeds):
    answer = []
    stack = []

    for p, s in zip(progresses, speeds):
        stack.append(math.ceil((100 - p) / s))

    if len(speeds) == 1:
        answer.append(1)
    else:
        start = 0
        check = 1
        end = len(stack)

        while True:
            if start == end:
                answer.append(1)
                break

            if check == end:
                answer.append(check - start)
                break

            if stack[start] >= stack[check]:
                check += 1
            else:
                answer.append(check - start)
                start = check

    return answer
