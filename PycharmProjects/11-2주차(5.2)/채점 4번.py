t=int(input())
i=1
while i<=t:
    num=[]
    i+=1
    a,b,c=map(int, input().split())
    num.append(a)
    num.append(b)
    num.append(c)
    for j in range(len(num)-1,-1,-1):
        for i in range(0,len(num[:j])):
            if num[i]>num[i+1]:
                num.insert(i+1,num.pop(i))
    for j in num:
        print(j, end=' ')

    # for j in range(len(num)-1):
    #     if num[j]<=num[j+1]:
    #         break
    #     else:
    #         num.insert(j+1,num.pop(j))
