import random

str_lotto=""

while len(str_lotto)<9:
    x = random.randint(1,45)
    if x < 10:
        x = "0" + str(x)
        if str_lotto[0:2] != x:  # 뭐랑 비교해야 함? [2:4] [4:6] 어떻게 쌓아나가야 함?
            str_lotto = str(x) + str_lotto
    else:
        str_lotto=str(x)+ str_lotto


print(str_lotto)