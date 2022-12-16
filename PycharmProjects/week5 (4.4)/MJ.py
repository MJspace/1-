num_str_a="1011"
num_str_b="11"

num_bin_a=[int(x) for x in num_str_a]
num_bin_b=[int(x) for x in num_str_b]

if len(num_bin_a) > len(num_bin_b):
    num_bin_b=[0] * (len(num_bin_a)-len(num_bin_b)) + num_bin_b
elif len(num_bin_a) < len(num_bin_b):
    num_bin_a=[0] * (len(num_bin_b)-len(num_bin_a))+num_bin_a


for i in range(len(num_bin_b)):
    if num_bin_b[i]:
        num_bin_b[i]=0
    else:
        num_bin_b[i]=1



Base=2
num_bin=[]
carry=0
num_bin_b[len(num_bin_b)-1]+=1
for index in range(len(num_bin_b)-1,-1,-1):
    bit_b=num_bin_b[index]
    sum_=bit_b+carry
    carry, r=sum_//Base, sum_%Base
    num_bin.insert(0,r)


Base=2
num_bin=[]
carry=0
for index in range(len(num_bin_a)-1,-1,-1):
    bit_a=num_bin_a[index]
    bit_b=num_bin_b[index]
    sum_=bit_a+bit_b+carry
    carry, r = sum_//Base, sum_%Base
    num_bin.insert(0,r)

l=0
while l<len(num_bin):
    if num_bin[0]==0:
        del num_bin[0]
    else:
        break
    l+=1

print(f"Binary number={num_bin}")
