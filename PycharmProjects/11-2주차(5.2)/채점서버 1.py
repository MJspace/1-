t=int(input())
i=1

while i<=t: #case
    i+=1
    a=int(input()) #받을 숫자 개수
    n = list(map(int, input().split()))
    print(sum(n))



    # while m<=a:
    #     m+=1
    #     num=[]
    #     b=map(int,input().split())
    #     num.append(b)
    #     print(sum(num))