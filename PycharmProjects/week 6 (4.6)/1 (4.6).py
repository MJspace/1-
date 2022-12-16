#empty list
list_=[]
#list_="" 이것도 가능
#if len(list_)==0:
if not list_:
    print("empty.")
else:
    print("not empty.")

#2.
numbers=[1,3,5,7,9,11]
l=numbers[1:4]

l[0]=100
print(l)
print(numbers)#l이랑 변화 있음 얘는 그대로 나옴 바꾸ㅣ지 않고고