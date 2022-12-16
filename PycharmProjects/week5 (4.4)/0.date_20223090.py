#y,m,d = map(int, input().split())
print("오늘의 날짜를 입력하시오")
y=int(input("Year : "))
m=int(input("Month : "))
#윤년 갯
d=int((input("Date : "))수 판단
leap year=y//4-y//100 #+y//400
#2월달 판단 + 30,31 판단

if (y%400==0) or ((y%4==0) and (not(y%100==0))) : #and first compare, or next compare
#
n=leap year*366+365*(y-leap year)+ d


