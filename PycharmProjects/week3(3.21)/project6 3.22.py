import math
#num_dec=0 일땐 어쩌지를 고민!
BASE=2
num_dec= 51 #input
print(f"Decimal number = {num_dec}") #{변수} 인거임,f는 변수임을 인식하게 함

num_bin="" #output 여기에 결과가 쌓임

if num_dec< BASE:
    num_bin=num_dec
else:
    while num_dec > 0 : # 3번 돔
        num_dec, r = num_dec // BASE, num_dec % BASE
        num_bin = str(r) + num_bin

print(f"Binary number={num_bin}")
