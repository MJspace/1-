
def mul(n):
    a = len(n)
    b=1
    for i in range(a):
        if n[i]==0:
            pass
        else:
            k=n[i]
            b*=k

    num=[]
    for j in str(b):
        num.append(int(j))

    if len(num)!=1:
        return mul(num)
    else:
        return num[0]

t=int(input())
for j in range(t):
    num_ = list(map(int, input()))
    print(mul(num_))

