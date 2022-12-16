import random

str_lotto=""

while len(str_lotto)<9:
    x = random.randint(1, 45)
    if x < 10:
        x = "0" + str(x)
        if x[0:2] != random.randint(1,45): #뭐랑 비교해야 함? [2:4] [4:6] 어떻게 쌓아나가야 함?
            str_lotto=str(x)+str_lotto
        else:          #같을 경우 비교해야 함 다시 돌려야 함. 근데 그걸 어떻게 다시 돌리는 걸로 올리지



print(str_lotto)