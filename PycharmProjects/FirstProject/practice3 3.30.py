str_="Hello" #문자열=시퀀스, 따라서 str_[0]이것처럼 인덱스를 가지고 접근할 수 있음

for i in str_:
    print(i) #처음 돌리면 1, 2번째 돌리면 2, 3번째 돌면 3번째 인덱스인 5를 가져옴
print("done")

for i in [1,2,5]:
    print(i) #처음 돌리면 1, 2번째 돌리면 2, 3번째 돌면 3번째 인덱스인 5를 가져옴
print("done")

#2.
l=[0,1,2,3]
cnt_iter=0
while cnt_iter<len(l):
    print(l[cnt_iter])
    cnt_iter+=1

cnt_iter=lent(l)
while cnt_iter>=0:
    print(l[cnt_iter])
    cnt_iter -=1

#3.
for i in range(0,10):
    print(i) #인덱스임

for i in range(10,0,-2): #lst []느낌임,결국 인덱스임, 10부터 1까지 -2씩 줄여나마감
    print(i)