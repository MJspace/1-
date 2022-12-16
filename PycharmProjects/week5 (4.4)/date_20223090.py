#y,m,d = map(int, input().split())
print("오늘의 날짜를 입력하시오")
y=int(input("Year : "))
m=int(input("Month : "))
d=int(input("Date : "))

month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
week=['일요일','월요일', '화요일', '수요일', '목요일', '금요일', '토요일']

for i in range(1,y):
    if (y % 400 == 0) or ((y % 4 == 0) and (not (y % 100 == 0))):  # and first compare, or next compare
        d+=366
    else:
        d+=365
#땡
for j in range(1,m):
    if(y % 400 == 0) or ((y % 4 == 0) and (not (y % 100 == 0))):
        month[2]=29
    d+=month[j]

print(week[d%7])








