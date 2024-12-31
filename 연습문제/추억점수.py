name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]

def solution(name, yearning, photo):
    result = [0]* len(photo)
    for person in photo:
        answer=0
        for p in person:
            if(p not in name): continue
            answer += yearning[name.index(p)]
            result[photo.index(person)] = answer
    return result

print(solution(name,yearning,photo))