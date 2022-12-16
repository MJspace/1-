def solution(_string): #_string 자체에 인덱스 할 수 있음
    answer=''
    for i in _string: #str인 _string을 한 글자씩 읽어 감
        if i==i.upper():
            answer+=i #문자열끼리는 더할 수 있음
    return answer
print(solution("PyThon"))