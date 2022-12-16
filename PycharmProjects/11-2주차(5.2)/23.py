count = int(input())
for i in range(count):
    sum_ = 1
    num = input()
    while len(num) > 1:
        for j in num:
            if int(j) != 0:
                sum_ *= int(j)
            else:
                continue
        num = str(sum_)
        if len(num) != 1:
            sum_ = 1
    print(sum_)
