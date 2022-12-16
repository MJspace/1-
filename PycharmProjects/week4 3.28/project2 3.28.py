phi=3.14
x=3
y=4
print("X=%d" % x) # 중간에 2번째 % 앞에 ,콤마 찍으면 안됨! 문법임
print("Hello, %s" % input())
print("Hello, %s" % "five")
print("Hello, %c"% "ABC") #이건 성립 안됨->
print("Hello, %f%%" % 30.1234) #

print("{}".format("five"))
#str_01="{}".format("five")
data="five"
str_01=f"{data}"

print("{}".format("five"))
print("{}".format("A"))
print("{}".format(3))
print("{}%".format(3.32))
print("{:f}%".format(3))
print("{z} {y} {x}".format(x=3, z=255, y=10))


print(str_01)