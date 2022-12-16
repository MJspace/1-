import math
n=100
m=math.log(n+1)
print("ln(n+1)의 측정값 :", m)

k=0
for i in range(1,101): #keep summing
        k+=1/i
print("조화급수의 실제값 :", k)

e=(m-k)/k
print("오차율 :", e)
