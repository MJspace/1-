BASE = 16
num_dec = 16266
print(f"Decimal number: {num_dec}")
num_hex = ""

if num_dec<10:
    num_hex=num_dec
else:
    while num_dec > 0:
        num_dec, r = num_dec // BASE, num_dec % BASE  # ,를 기준으로 분배법칙 느낌
        if r == 10:
            r = "A"
        elif r == 11:
            r = "B"
        elif r == 12:
            r = "C"
        elif r == 13:
            r = "D"
        elif r == 14:
            r = "E"
        elif r == 15:
            r = "F"
        num_hex = str(r) + num_hex
print(f"Hexadecimal number: {num_hex}")
