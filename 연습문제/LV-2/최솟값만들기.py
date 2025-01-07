A = [1, 4, 2]
B = [5, 4, 4]

def solution(A,B):
    A.sort(reverse=False)
    B.sort(reverse=True)
    sum=0
    for i in range(len(A)):
        sum+=A[i]*B[i]
    return sum

print(solution(A,B))