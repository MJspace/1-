n=int(input("n>"))

for i in range(n+1):
    for j in range(n-i):
        print(end=' ')
    for j in range(2*i-1):
        print("*", end='') #end 이용해서 세로로 나열될 것을 가로로 나열되게 함
    print() #enter의 역할을 해서 쌓아주는 역할