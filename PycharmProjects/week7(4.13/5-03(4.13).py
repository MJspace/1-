data={1:"a",(1,2,3):"b"}

for key in data:
    print(key, data[key])
for value in data.values():
    print(value)
#key,value=item(튜플)
for item in data.items():
    print(item[0], item[1])

student=(2012,"Kim",30)
id, name, age=student
print(id,name,age)

data={1:"a", 2:"b", 3:"c", "KMU":"Hello"}
if 3 in data:
    print(data[3])
else:
    print("error")

#del data-> 다시는 data 접근할 수 없음
print(data.get(3))

numbers={1,2,3,4}
print("before:", numbers)
numbers.update((5,6,7,3,4))
ret=numbers.pop()
print("after:", numbers,ret)