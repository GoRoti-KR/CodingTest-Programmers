def solution(n):
    sum = 0
    while(True):
        sum += n%10
        n//=10
        if(n//10==0):
            sum += n%10
            break
    return sum

# print(solution(10000000024))
def sum_digit(number):
    return sum([int(i) for i in str(number)])

print("Result :", sum_digit(123))