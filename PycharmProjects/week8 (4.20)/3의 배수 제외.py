# def solution(n):
#     sum_ = 0
#     for num in range(n+1):
#         # if num%3==0:
#         #     num=0
#         #     sum_+=num
#         sum_+=num
#     for num in range(n+1):
#         if num%3==0:
#             sum_-=num
#     return sum_

def solution(n):
    sum_= 0
    for i in range(n+1):
        if i%3!=0:
            sum_+=i
    return sum_
print(solution(10))

def solution(n):
    sum_= 0
    for i in range(n+1):
        if i%3==0:
            i=0
        else:
            sum_+=i
    return sum_
print(solution(10))

def solution(n):
    sum_= 0
    for i in range(n+1):
        if i%3==0:
            continue #i가 3의 배수이면, sum_+=i 실행하지 말고 다시 for문으로 돌아감
        sum_+=i
    return sum_
print(solution(10))


