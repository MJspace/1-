import time
import random

low=0
high=1000
iter=1000
a=[]
for i in range(iter):
    a.append(random.randint(low,high))
b=a#정렬 안된 리스트
start=time.time() #정렬하기 전의 시간
a.sort() #정렬됨
 #정렬한 후의 시간

print("sort : ", end='')
print(a)
print("Running sort(%d) takes %s" %(iter, (time.time()-start)))


start=time.time()
for j in range(len(b)-1,-1,-1):
    for i in range(0,len(b[:j])):
        if b[i]>b[i+1]: #비교, 클 때만 생각하면 됨
            b.insert(i+1,b.pop(i))

end=time.time()
print("bubble : ", end='')
print(b)



print("Running bubble(%d) takes %s" %(iter,end-start))




