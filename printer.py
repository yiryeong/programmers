from collections import deque


def solution(priorities, location):
    answer = 0
    pdq = deque(priorities)
    ldq = deque([0] * len(priorities))
    ldq[location] = 1

    pd_pop = pdq.popleft()
    ld_pop = ldq.popleft()

    while True:
        if not pdq:
            answer += 1
            break

        if pd_pop >= max(pdq):
            answer += 1
            if ld_pop == 0:
                pd_pop = pdq.popleft()
                ld_pop = ldq.popleft()
            else:
                break
        else:
            pdq.append(pd_pop)
            ldq.append(ld_pop)
            pd_pop = pdq.popleft()
            ld_pop = ldq.popleft()

    return answer
