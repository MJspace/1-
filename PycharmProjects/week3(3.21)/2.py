BASE=16
num_dec=60
print(f"Decimal number={num_dec}")

num_hex=""

if num_dec<10:
    num_hex=num_dec
else:
    while num_dec>=10:
        num_dec, r=num_dec // BASE, num_dec%BASE #몫, 나머지 #이 num_hex는 어디서 오는거?
        if r == 10:
            num_hex = "A"
        elif r == 11:
            num_hex = "B"
        elif r == 12:
            num_hex = "C"
        elif r == 13:
            num_hex = "D"
        elif r == 14:
            num_hex = "E"
        elif r == 15:
            num_hex = "F"
        num_hex = str(r) + num_hex
print(f"hexadecimal number={num_hex}")