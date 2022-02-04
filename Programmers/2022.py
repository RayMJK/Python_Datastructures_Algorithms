def solution(answers):
    answer = []
    #print(answers)
    a1 = [1,2,3,4,5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a1_count = 0
    a2_count = 0
    a3_count = 0
    result = []
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        if answers[s1] == a1[i]:
            a1_count += 1
        if answers[s2] == a2[i]:
            a2_count += 1
        if answers[s3] == a3[i]:
            a3_count += 1
    result.append(a1_count)
    result.append(a2_count)
    result.append(a2_count)
    max_answer = max(result)
    if a1_count == max_answer:
        answer.append(1)
    if a2_count == max_answer:
        answer.append(2)
    if a3_count == max_answer:
        answer.append(3)
    return answer