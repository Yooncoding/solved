from itertools import combinations

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    for i in combi:
        if isPrime(sum(i)):
            answer += 1
    return answer
