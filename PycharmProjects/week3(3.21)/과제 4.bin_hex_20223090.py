num_bin="000101000010"
#101101110011
print(f"Binary numbr={num_bin}")

BIT=4 #변수
num_bin=num_bin[::-1] #1    0   1   1 #역수취하는 것
                #2^0    2^1     2^2 2^0Z

num_hex= ""
cnt_bit=0 #변수
while cnt_bit < len(num_bin): #길이
    cnt=0
    sum_=0
    while cnt<BIT and cnt_bit <len(num_bin) : #4비트씩 끊어 읽어주는 문장
        sum_+=2**cnt * int(num_bin[cnt_bit])
        cnt+=1
        cnt_bit+=1
        if sum_ == 10:
            sum_ = "A"
        elif sum_== 11:
            sum_ = "B"
        elif sum_ == 12:
            sum_ = "C"
        elif sum_ == 13:
            sum_ = "D"
        elif sum_ == 14:
            sum_ = "E"
        elif sum_ == 15:
            sum_ = "F"

    num_hex=str(sum_)+num_hex

print(f"Hexadecimal number={num_hex}")