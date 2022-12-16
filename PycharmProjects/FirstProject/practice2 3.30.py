#1. 그냥 내멋대로 한 것
x=int(input("연도를 입력하시오:"))

if x/4==0:
    print("윤년입니다.")
elif x/100==0:
    print("윤년이 아닙니다.")
elif x/400==0:
    print("윤년입니다.")

#2. 교수님과 함께한 것

year=2022

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("%d is a leap year." % year)
        else:
            print("%d is not a leap year." % year)
    else:
        print("%d is a leap year." % year)

else:
    print("%d is not a leap year." %year)

#3. 논리연산자로 수정
year=int(input())
if (year%400==0) or ((year%4==0)and (not(year%100==0))):
    print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)


