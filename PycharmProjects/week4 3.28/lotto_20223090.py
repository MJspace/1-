import random

str_lotto=""
y=""

while len(str_lotto)<9:
    x = random.randint(1, 45)
    if x < 10:
        x = "0" + str(x)
    if str_lotto[0:2]!=x and str_lotto[2:4]!=x and str_lotto[4:6]!=x and str_lotto[6:8]!=x and str_lotto[8:10]!=x:
        str_lotto = str(x)+str_lotto
        y = str(x)+" "+y

print(y)







