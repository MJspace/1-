import math
n=50
lst=[]
a=int(math.sqrt(n)) #root
for i in range(1,n+1):
    lst.append(i)

p=[]
for i in range (2,a+1):
    p.append(i) #[2,3,4,5,6,7]

m=[]
# 위의 구한 값 사이에서 소수 찾음
for i in range(len(p)): #0~5
    b=p[i] #type=int
    while b <= a: #a=7
        b+=p[i] #b=2->4,6 b=3->6
        if (b in p) and (b not in m): #위 두 조건 모두 만족하면 m에 쌓여서 list m에 없으면 다시 누적 ex.6
            m.append(b) #m[4,6]

prime=set(p)-set(m) #[2,3,5,7]

#배수를 지워나감
for i in range(len(prime)): #0~3
    b=list(prime)[i] #set->list로 바꿔줌
    while b < 50:
        b+=list(prime)[i] #위에처럼 똑같이 계속 누적 빼기 2->4,6,8,10,,,,,,,
        if b in lst: #겹치는 게 나와도 이미 리스트에서 없어졌으니깐 또 지우지 x
            lst.remove(b)
lst.remove(1)
print(lst)







