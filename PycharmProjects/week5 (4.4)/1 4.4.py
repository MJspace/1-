import time
n=10
bgn_time=time.time()
for i in range(2,n):
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number") #if가 아닌 for문에 묶인 거임. 만약 if절 만족하면 range 처음부터 끝까지 돌필요 없음. 근데 만족못하면 range 처음부터 끝까지, 즉 2부터 n-1까지 다 돌아
print(f"d_time={time.time()-bgn_time}")

import time

lst=[1,2,3,4]
lst[2]=100
print(lst)

r=range(0,10)
#r[3]=900 저장자체가 안되기에 쓸 수 없음
print(list(r))#print(r)->아직 메모리가 없기 때문에 연산 못함

num=100
while True:
    if num==100:
        continue#break이면 헬로 출력 하지 않음, continue이면 출력안하고 곧장 와일로 다시 돌아옴
    print("hello")
    print("world")
