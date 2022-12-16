dict_={1001:"Alice", 1002:"Bob", "KMU":"Kim"}
print(dict_[1001])
#key값만 쓸 수 있고, index는 쓸 수 없음 시컨스가 아니기 때문
print(dict_["KMU"])
for key in dict_.keys():
    print(key, dict_[key])

for item in dict_.items():
    print(item[0], item[1])

for key, val in dict_.items():
    print(key,val)

for key in dict_.items():
    print(key)

if 2001 in dict_:
    print(dict_[2001])
else:
    print("Error")

res=dict_.get(2001)
print(res)#2001의 여부 먼저 확인할 필요x, 그냥 없으면 none이야

res=dict_.get(2001,-1)
print(res)#이때는 없을 경우 none이 아닌 -1값 도출

res=dict_.pop(1001) #lst처럼 ()놔두면 알아서 뒤에것 지워지는 게 아닌게 아닌 인덱스 값 넣어줘야 함
print(dict_)