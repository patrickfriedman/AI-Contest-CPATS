def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    for digit in binary:
        if digit == '0':
            current_gap += 1
        else:
            if current_gap > 0:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
    return max_gap