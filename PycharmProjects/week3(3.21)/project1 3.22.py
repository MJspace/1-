BASE=2
num_dec=11 #input
print(f"Decimal number = {num_dec}") #{변수} 인거임,f는 변수임을 인식하게 함

num_bin="" #output 여기에 결과가 쌓임

#1. 11 num_dec=num_dec//BASE r=num_dec%BASE #나머지  +바로 상수 들어가면 안좋음 따라서 2대신 BASE가 들어감 여기서 num_dec=5
num_dec, r=num_dec//BASE, num_dec%BASE
num_bin=str(r)+num_bin #정수 +문자열 안됨 따라서 r을 문자열로 바꿔야 함

#2. 5
num_dec, r=num_dec//BASE, num_dec%BASE
num_bin=str(r)+num_bin

#3. 2
num_dec, r=num_dec//BASE, num_dec%BASE
num_bin=str(r)+num_bin

num_bin=str(num_dec) + num_bin
print(f"Binary number={num_bin}")

print(num_bin)
print(type(num_bin))




