def solution(a, b):
    answer = ''
    calender = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    count = 0

    for month in range(1, a):
        print(month, months[month])
        count += months[month]
    count += b
    count -= 1
    result = count % 7
    date = calender[result]
    answer += date

    return answer
print(solution(5, 24))