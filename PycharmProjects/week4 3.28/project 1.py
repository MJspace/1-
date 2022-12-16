name=input()
print(f"Received: {name}")

data=input("Enter a number :")

print(type(data)) #data는 문자열 -> 바로 밑에 줄 출력에 data+10 못함, 그래서 앞에 int 씀

print(f"Received: {data}")
print(f"Received: {data + str(10)}") #문자열끼리 합이니깐 쓰여진 대로 산술필요 없이 보이는 대로 씀
data=int(data) #data=int(input("Enter a number :"))로 바로 바꿔버려도 가능
print(f"Received: {data + 10}") #str data를 int로 바꿨기 때문에 덧셈으로 계산! 보이는 대로 쓰지 않아!

somebody=input("Enter a name:")
print("Hi", somebody)
age=int(input("How old r u?"))
print()

x="hello"*3
print(len(x)) #길이

print("Good\n"+"morning")
print("Good\f"+ "morning")
print("Good\t"+"morning\n"+"hello")
print("Hello", end="\b\n")
print("\'hello\'") #작은 따옴표 쓰고 싶어 ("'hello'")
print("\\hello") #\를 출력하고 싶음

data="hello"
print("%s" % data) #이건 성립 근데 s->c가 되면 성립하지 않음


