t=int(input())
for j in range(t):
    n=list(map(int,input()))
    a=len(n)
    mul=1
    for i in range(a):
        if n[i]==0:
            pass
        else:
            k=n[i]
            mul*=k
    print(mul)


