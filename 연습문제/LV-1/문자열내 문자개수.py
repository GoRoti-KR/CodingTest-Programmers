def solution(s):
    count = [0,0]
    for word in s:
        if(word=="p"or word=="P"): count[0]+=1
        elif(word=="y" or word=="Y"): count[1]+=1
    if(count[0]==count[1]): return "true"
    else: return "false"

print(solution("pPoooyY"))