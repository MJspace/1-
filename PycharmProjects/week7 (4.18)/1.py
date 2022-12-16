# data=[1,2,3,4,5]
# data_copy=data
# print(id(data))
# print(id(data_copy))
# data_copy[0]=999
# print(data)

def foo(data_):
    print(id(data_))
    pass

data=[1,2,3,4,5]
print(id(data))
foo(data)

def calculateTax(price, tax_rate) :
    total=price+(price*tax_rate)
    return total
my_price=float(input("Enter a price:"))
totalPrice=calculateTax(my_price, 0.06)

print("price=", my_price,"Total price=", totalPrice)


n=5
def sigma(n):
    ret=0
    for i in range(1,n+1):
        ret+=i
    return ret
def sigma_rec(n):
    if n==1:
        return n
    return n + sigma_rec(n-1)
print(n, sigma_rec(n))

def fact(n):
    if n==0:
        return 1 #어차피 이 조건 만나면 바로 return 1 하니깐
    return n*facto(n-1) #else, 즉 if n=0인 경우

n=5
print(n, fact(n))

 #0 1 1 2 3 5 8 13 21 34 55   1+1 1+2 2+3 3+5 5+8
def fibo(n):
    if n==0 or n==1:
        return n
    else: #return fibo(n-1) + fibo(n-2)
        return fibo(n-1) + fibo(n-2)
n=10
print(n, fibo(n))

# def fibo(n):
#     if n==0 or n==1:
#         return n
#     prev, pprev=0,1
#     for i in range(0,n-1):
#         prev, pprev =pprev, prev+pprev
#     return pprev
#
# n=10
# print(n, fibo(n))