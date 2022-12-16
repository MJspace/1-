import math

BASE=2
num_dec=11#input
print(f"Decimal number = {num_dec}") #{변수} 인거임,f는 변수임을 인식하게 함

num_bin="" #output 여기에 결과가 쌓임

while num_dec>=BASE : # 3번 돔
    num_dec, r = num_dec // BASE, num_dec % BASE
    num_bin = str(r) + num_bin

num_bin=str(num_dec) + num_bin
print(f"Binary number={num_bin}")
