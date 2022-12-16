#나머지가 10이상이면 알파벳, 10미만이면 그대로

BASE=16
num_dec=16266
print(f"Decimal number={num_dec}")

r=num_dec // BASE
num_hex=""
if r==10:
    num_hex="A"
elif r==11:
    num_hex="B"
elif r==12:
    num_hex="C"
elif r==13:
    num_hex="D"
elif r==14:
    num_hex="E"
elif r==15:
    num_hex="F"

if num_dec<10:
    num_hex=num_dec
else:
    while num_dec>=10:
        num_dec, r=num_dec // BASE, num_dec%BASE #num_dec=r
        num_hex=str(r)+num_hex
print(f"hexadecimal number={num_hex}")
