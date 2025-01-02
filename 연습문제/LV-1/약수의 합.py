import math

def solution(n):
    answer = []
    i = 1
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            answer.append(i)
            if i != n // i:
                answer.append(n // i)
        i += 1
    return sum(answer)

print(solution(12))