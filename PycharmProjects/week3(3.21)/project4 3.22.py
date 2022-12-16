#10->2진수한것을 10->8진수로
import math

BASE=8
num_dec=11#input
print(f"Decimal number = {num_dec}") #{변수} 인거임,f는 변수임을 인식하게 함

num_bin="" #output 여기에 결과가 쌓임

#cnt_iter=3 #반복횟수 -> 큰 수가 나왔을 때는 어떻게? 그래서 로그 씀
cnt_iter=int(math.log(num_dec,BASE)) #우리는 정수만 필요 따라서 실수->정수로 변환
while cnt_iter>0 : # 3번 돔
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin
    cnt_iter -= 1

num_bin=str(num_dec) + num_bin
print(f"Binary number={num_bin}")
