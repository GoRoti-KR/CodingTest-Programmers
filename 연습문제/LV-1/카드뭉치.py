cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

def solution(cards1, cards2, goal):
    cnt1,cnt2=0,0
    for word in goal:
        if(cnt1<len(cards1) and cards1[cnt1]==word): cnt1+=1
        elif(cnt2<len(cards2) and cards2[cnt2]==word): cnt2+=1
        else: return "No"
    return "Yes"

print(solution(cards1, cards2, goal))