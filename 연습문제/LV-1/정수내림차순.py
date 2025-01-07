n=123

def solution(n):
    answer=0
    number = list(map(int,list(str(n))))
    number.sort(reverse=True)
    print(number)
    for i in range(len(number)):
        answer += number[i] * (10 ** (len(number) - i - 1))     
    return answer

print(solution(n))