p=int(input())
for j in range(p):
    n = input()
    n_list = list(map(int, str(n)))
    k = len(n_list)
    sum_ = 0
    for i in range(len(n_list)):
        v = n_list[i] ** k
        sum_ += v  # sum=sum+v

    if sum_ == int(n):
        print(1)
    else:
        print(0)
