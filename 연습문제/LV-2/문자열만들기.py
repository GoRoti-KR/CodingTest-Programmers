s="hI niCe to meet you"

def solution(s):
    words = s.lower().split(" ")
    for i in range(len(words)):
        if words[i] and words[i][0].isalpha():
            words[i]= words[i][0].upper() + words[i][1:]
    return " ".join(words)

print(solution(s))