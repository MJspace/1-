list_=[1,2,3,4]
#result=[n*2 for n in range(1,11)]
#print(result)
list_.sort(reverse=True) #list[::-1] 이것과 다름
print(list_)

list_=["a","d","c","addd"]
list_.sort() #컴퓨터에 디폴트 되어 있는 기준으로 바뀜

list_=["a","d","b","addd"]
print(list_)
list_copy=list_[:]
list_copy.sort()
print(list_copy) #원본은 따로 유지하고 이건 유지 안하고 디폴트 값으로 바꾸고 싶을 때
print(list_) #원본유지

list_=[8,4,9,5]
small=list_[0]
for n in range(0,len(list_)-1):
    if small>list_[n+1]:
        small=list_[n+1]
print(small)
print(max(list_))