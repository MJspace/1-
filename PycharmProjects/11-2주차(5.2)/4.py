t = int(input())
i = 1
while i <= t:
    num = []
    i += 1
    a, b, c = map(int, input().split())
    if a <= b:
        if b <= c:
            print(a, b, c)
        else:
            if a <= c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if c <= b:
            print(c, b, a)
        else:
            if a <= c:
                print(b, a, c)
            else:
                print(b, c, a)


