s = "1 -2 -3 4"

def solution(s):
    count = list(map(int, s.split()))
    return str(min(count)) + " " + str(max(count))

print(solution(s))



## map 함수 사용
### map(function[적용할 함수], iterable[함수에 적용할 데이터 집합])
### map(int, s.split())  >> 공백을 기준으로 list로 저장한 s 문자열을 대상으로 int 함수를 적용 

## split(standard[나누는 기준]) >> 특정한 기준에 따라 나눔
### string.split() >> 공백   |  string.split(":") >> : 기준으로 나눔   >> 나누는 기준은 삭제되고 문자열은 list로 저장됨