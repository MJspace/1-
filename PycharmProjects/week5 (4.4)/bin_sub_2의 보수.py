num_str_a="1011"
num_str_b="11"

num_bin_a=[int(x) for x in num_str_a] #리스트에 자리마다 숫자 삽입해서 이런식으로 변형하고 정수로 바꿔줌  ['1','0','1','1']
num_bin_b=[int(x) for x in num_str_b]

if len(num_bin_a) > len(num_bin_b): #자릿수를 맞춰서 앞에 0을 필요한 숫자만큼 붙여줌
    num_bin_b=[0] * (len(num_bin_a)-len(num_bin_b)) + num_bin_b #b가 더 짧을 경우
elif len(num_bin_a) < len(num_bin_b): #a가 더 짧을 경우
    num_bin_a=[0] * (len(num_bin_b)-len(num_bin_a))+num_bin_a #두 num_bin a(작은 수) num_bin b(큰수)의 길이 차이(len)만큼  앞부분부터 [0]을 채워 줌 그 후에 작았던 num_bin_a를 붙여줌

#1의 보수
for i in range(len(num_bin_b)): #b가 더 짧을 경우 (*무조건 0과 1로 구성됨), 0부터 위에서 큰수에 자리 맞춰줬으니 0011 즉 0~3자리
    if num_bin_b[i]: #true=1 값을 받아와서 작동하고, false=0이므로 작동하지 않음, 0일 경우 false이므로 else로 들어감
        num_bin_b[i]=0
    else:
        num_bin_b[i]=1


#2의 보수, +1을 취하고 올림수를 이용, 이진수 덧셈 이용
Base=2
num_bin=[]
carry=0
num_bin_b[len(num_bin_b)-1]+=1 #맨 오른쪽에 +1 하는 것
for index in range(len(num_bin_b)-1,-1,-1): #반대쪽으로 0까지 len로 길이 판별해서 짧은 거에 1붙여줌
    bit_b=num_bin_b[index]
    sum_=bit_b+carry
    carry, r=sum_//Base, sum_%Base #올림수 처리
    num_bin.insert(0,r)

#2진수 뺄셈->carry=올림수, carry 맨 앞자리 올림수는 신경쓰지 말고 나머지 부분만 신경쓰면 됨 즉 큰수에서 2의 보수 더하면 11000인데 맨 앞 올림수인 1은 무시
Base=2
num_bin=[]
carry=0
for index in range(len(num_bin_a)-1,-1,-1): #3~0 1011, 1101
    bit_a=num_bin_a[index]
    bit_b=num_bin_b[index]
    sum_=bit_a+bit_b+carry #원래 큰수+2의 보수로 바꾼 작은수+올림수, carry 값은 계속 갱신됨 그래서 전에 있던 carry 값 있으면 그거 더함
    carry, r = sum_//Base, sum_%Base #carry=몫, r=나머지
    num_bin.insert(0,r) #위에 정의한 num_bin 리스트에 0의 자리에 계속 나머지 값을 쌓아줌 마지막 carry는(즉 맨앞)은 무시->이 결과값=1000

l=0
while l<len(num_bin): #len=4 l이 0~3까지
    if num_bin[0]==0: #만약 0110일 경우 [0]=0, 00110일 경우는 반복해서 지워줌 00110->0110->110
        del num_bin[0] #0101일 경우 0을 없애서 101로 만드는 작업
    else:
        break
    l+=1

print(f"Binary number={num_bin}")
