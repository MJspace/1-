t=int(input())
i=1

while i<=t: #case
    i+=1
    a=int(input()) #받을 숫자 개수
    n = list(map(int, input().split()))
    print(max(n), min(n))
