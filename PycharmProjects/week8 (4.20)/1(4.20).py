def foo(param):
    param[0]=100
    print(param)
    pass

*list_,=range(0,10)
foo(list_[:])
foo(list_)
#1.
get_sum=lambda x,y:x+y
#2.
res=get_sum(10,20)
print(res)

re=(lambda x,y:x+y)(10,20)
print(res) #근데 이렇게 하면 인자 바꿀때마다 lambda 형식 반복적으로 계속 써줘야 함-> 함수이름 정해서 호출해주는 게 더 나음

#3.
a=[("Yoon",2010), ("Kim",2006),("Lim",2004)]
for n,y in a:
    print(n,y) #튜플이라 언팩킹 가능
print(a[0][0]) #튜플은 인덱스로 access 가능
a.sort()
print(a)
a.sort(key=lambda x: x[1])
print(a)


#4.
members = ["김성규", "장동우","남우현", "이성열","엘","이성종"]
print(members)

for number, name in enumerate(members):
    print(number, name)

for number, name in enumerate(members, start=1):
    print(number, name) #언패킹된것

for i in enumerate(members, start=1):
    print(i[0], i[1]) #패킹

#5.
student=[
    ("허준녕",20153253,4.2),
    ("김영재",20153180,3.7),
    ("한채연",20153250,4.5)
]
print("before")
print(student)
print("After")
sorted_=sorted(student,key=lambda x:x[1])
print(sorted_)

student={
    20153180,3.7,
    20153250,4.5,
    20153253,4.2
}
for i in student.items(): #i==key
    print(i) #튜플임 packing

sorted_=sorted(student)
print(sorted_) #기준 없어서 맨 앞 인덱스만 나열됨

sorted_=sorted(student.items(), key=lambda x:x[1])
print(sorted_)

