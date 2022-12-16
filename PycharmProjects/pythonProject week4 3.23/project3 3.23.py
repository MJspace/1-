num_bin="1101" #2^3 2^2 2^1 2^0, type=str
print(f"Binary number={num_bin}")

num_bin=num_bin[::-1] #역수로 바꾸겠다는 뜻 1011 2^0 2^1 2^2 2^3

cnt_iter=0 #4번 4비트니깐
num_dec=0
while cnt_iter < len(num_bin):
    print(cnt_iter)
    num_dec+=2**cnt_iter * int(num_bin[cnt_iter])#2^0*1 2^1*0 2^2*1 2^3*1 str로 접근했기때문에 정수로 변환
    # #역순으로 가야함
    cnt_iter += 1
print(f"Decimal number={num_dec}")