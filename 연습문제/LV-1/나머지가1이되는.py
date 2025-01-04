def solution(n):
    i=1
    while(i<int(n**0.5+1)):
        if(n%i==1):
            return i
        else:
            i+=1
    return n-1

## 시간단축을 위해 제곱근 까지만 탐색한다
### 어차피 제곱근 전에도 없으면 후에도 없기 때문
#### 그래서 제곱근을 넘어가면 자기자신에서 1을 뺀걸 return 한다