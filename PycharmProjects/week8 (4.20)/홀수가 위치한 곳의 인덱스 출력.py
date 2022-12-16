n=list(map(int,input().split()))
ans=[]
for i in range(len(n)):
    if n[i]%2==1:
        ans.append(i)
if len(ans)==0:
    ans.append(-1)

for i in ans:
    print(i,end='') #->정수로 나옴
# print(ans) -> 리스트로 나옴