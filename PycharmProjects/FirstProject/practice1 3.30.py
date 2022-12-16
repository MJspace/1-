#1.
import datetime #시간 구하는 소요시간도 포함 함수
time_now=datetime.datetime.now() #객체 time_now가 지원하는 게 또 있음, 그걸 이용
print(time_now)

if time_now.hour<12:
    print("AM")
else:
    print("PM")

#2. 3항 연산자로 바꿔보자
import datetime #시간 구하는 소요시간도 포함 함수
time_now=datetime.datetime.now() #객체 time_now가 지원하는 게 또 있음, 그걸 이용
print(time_now)

str_="AM" if time_now.hour<12 else "PM"
print(str_)
