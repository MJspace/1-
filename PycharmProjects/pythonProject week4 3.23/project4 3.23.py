num_bin="1011" #
print(f"Binary number={num_bin}")

num_bin=num_bin[::-1] #1    0   1   1
                #2^0    2^1     2^2 2^0
cnt_iter=0 #4번 4비트니깐
num_oct= ""
BIT=3
cnt_bit=0
while cnt_bit < len(num_bin):
    cnt=0
    sum_=0
    while cnt<BIT:
        if cnt_bit>=len(num_bin):
            break #go to line 20

        sum_+=2**cnt * int(num_bin[cnt_bit])
        cnt+=1
        cnt_bit+=1
    num_oct=str(sum_)+num_oct

print(f"Octal number={num_oct}")