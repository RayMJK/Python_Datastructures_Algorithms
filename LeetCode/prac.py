def solution(strings, n):
    answer = []
    result = dict()
    for i in strings:
        result[i] = i[n]
    print(result)
    result = sorted(result.items(), key=lambda x:x[1])
    result = sorted(result, key = lambda x : (x[1], x[0]))
    return result
strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n))