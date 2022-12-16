# 1.
print("Enter your age:")
age=input() #아니면 아예 if에 int 안쓰고, int(input())으로 바꿀 수 있음
print("Enter your score:")
score=input() #아니면 아예 if에 int 안쓰고, int(input(Enter your score:))으로 바꿀 수 있음

if int(age) > 19 and float(score) >90:
    print("you are allowed to enter.")
else:
    print("your are not allowed.")

#2.
x=10
is_under_20 #10<20
print("is_under_20", is_under_20) #true
print("not_is_under_20", not is_under_20) #false

#3.
x=20
if x>10:
    y=x*2
else:
    y=x/2
print(y)

#3.-> 3항 연산자로 바꾼다면
x=20

y=x*2 if x>10 else x/2 #y=x/2처럼 y를 써주면 안됨. 연산자는 앞에 저으이 함
print(y)


