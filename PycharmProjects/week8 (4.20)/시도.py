# _string=[1,2,3]
# for i in range(len(_string)):
#     print(i)

# def f(n):
#     x=2
#     for i in range(1,n+1):
#         x*=i
#
#     return x
# print(f(3))
#
# a='name'
# b='age'
# c=a+" "+b
# print(c) str일때 ''던 ""던 상관 없음

# print("a\n"*2)
# print("a")
# print("a")
#
# # a,b=input().split() #split() 은 공백을 기준으로 나눔
# # print(int(a)+int(b))
# g=["ab","b","c"]
# print(len(g))
#
# a=int(input())
# if (a%4==0 and a%100!=0) or a%400==0:
#     print(1)
# else:
#     print(0)
# a,b = map(int, input().split())
# print(a+b)

# n=int(input())
# for i in range(n+1):
#     a,b=input().split()
#     a=int(a)
#     b=int(b)
#
# a=[1,2,3,4]
# result=[]
# for num in a:
#     result.append(num*3)
# print(result)

# N=int(input())
# for i in range(1,10):
#     print("%d * %d=%d" %(N,i,N*i))
t = int(input())
i = 1
while i <= t:
    num = []
    i += 1
    a, b, c = map(int, input().split())
    num.append(a)
    num.append(b)
    num.append(c)
    for j in range(len(num) - 1):
        if num[j] <= num[j + 1]:
            break
        else:
            num.insert(j + 1, num.pop(j))
    print(num)
