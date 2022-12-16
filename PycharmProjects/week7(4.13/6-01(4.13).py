def foo():
    #inside
    print("Hello")
    print("World")

#outside
re=foo()
print(re)

def print_my_info():
    print("My name is Minju.")
    print("I'm 21 years old.")
    print("Nice to meet you.")

print_my_info()
#
# def get_sum(args): #함수 이름 만들 때 동사가 앞에 옴
#     pass #pass를 해야 멀쩡하게 나옴, 아무의미 없음 그냥 이렇게 해야 함수 정의가 끝나는 것
# get_sum() #call the function

#           1       10
def get_sum(start, end):
    ret=0
    #                range(1, 10+1)
    for num in range(start, end+1):
        ret += num
    return ret
#main program
total=get_sum(1,10)
print(total)
# 함수 안 쓰면 이렇게 다 나열해서 써야 됨
# ret=0
# for num in range(1,10):
#     ret+=num
# print(ret)
#
# ret=0
# for num in rante(1,20):
#     ret+=num
# print(ret)
#
# #함수 쓰면 더 간결하게 쓸 수 있음
# re=get_sum(1,10)
# print(re)
#
# re=get_sum(1,20)
# print(re)

def get__sum(*args): #args의 타입=튜플
    ret=0
    for num in args:
        ret+=num
    return ret

re=get__sum(1,2,3,4,5,6,7)  #1 위 함수 정의에 *안 붙이면 sum(1)이런 식으로 하나씩 밖에 못함
print(re)

re=get__sum(1,2,3)    #2
print(re)


def print_my_info(n=1):
    for i in range(n):
        print("My name is Minju.")
print_my_info()
print("--구분선--")
print_my_info(3)

def foo(n=1): #n=1이 디폴트 값
    for i in range(n):
        print('hello')

foo(3)

def foo(l, n=1): #n=1이 디폴트 값, 이건 중간에 있을 수 없고 생략할 수 있음
    print(l)
    for i in range(n):
        print('hello')

foo(3,5)
