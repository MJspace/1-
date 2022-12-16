#ctrl / -> 주석 지우기
num_str_a="1011"
num_str_b="11"

num_bin_a=[int(x) for x in num_str_a] #리스트 입력
num_bin_b=[int(x) for x in num_str_b]

if len(num_bin_a) > len(num_bin_b): #길이 맞추기
    num_bin_b=[0] * (len(num_bin_a)-len(num_bin_b)) + num_bin_b  #1011, 0011
elif len(num_bin_a) < len(num_bin_b):
    num_bin_a=[0] * (len(num_bin_b)-len(num_bin_a))+num_bin_a

num_bin=[]
k=len(num_bin_a)-1 #리스트 값에 집어넣기 위해 -1을 취함. 리스트에서 마지막 값은 -1이니, k는 index 역할
while k>=0: #맨 오른쪽부터 탐색시킴
    bit_a=num_bin_a[k] #각 리스트 값 지정
    bit_b=num_bin_b[k]
    if bit_a>=bit_b: #인덱스 값이 num_bin_a가 num_bin_b보다 크거나 같을 경우->10/11/00
        num_bin.insert(0,bit_a-bit_b) #num_bin이라는 새로운 값에 순차적으로 그냥 뺀 수를 삽입
        k-=1 #오른쪽부터 왼쪽으로 탐색시키는 것
    else: #인덱스 값이 num_bin_a가 num_bin_b보다 작을 경우->01
        for i in range(len(num_bin_a[:k]),-1,-1): #num_bin_a를 k번째부터 0까지 반대로 돌아봄
            if num_bin_a[i]==1: #만약 num_bin_a의 값이 1일경우 이 1이 올림수 역할
                num_bin_a[i]=0 #위의 1이 올림수 역할 하니 1->0
                for j in range(i+1,k): #i와 k사이의 수를 1로 바꿔줌, 사이의 수는 0일 것
                    num_bin_a[j]=1
                num_bin_a[k]=2 #k의 수를 2로 바꿔줌
                break #올림수를 찾았으니깐, 여기는 제외하고(이미 한번 탐색 했으니 또 반복할 필요x) 앞부분 또 탐색 감, break 없으면 바꿔놨던 거 싹 다 1로 리셋 됨
                    #단 k값은 바뀌지 않음. 다시 while로 돌아가서 바뀐 수로 빼준 후 if 문에서 다시 k의 값을 else인 조건에 따라 지정
l=0
while l<len(num_bin):
    if num_bin[0]==0:
        del num_bin[0]
    else:
        break
    l+=1

print(f"Binary number={num_bin}")
#리스트 밖으로 빼내는 코드
print("Binary number=",end='') #end는 enter 역할
for i in range(len(num_bin)):
    print(num_bin[i],end='')