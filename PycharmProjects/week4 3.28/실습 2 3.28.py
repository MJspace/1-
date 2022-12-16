from urllib.request import urlopen

f=urlopen("https://www.python.org")  #f=변수
print(f.headers)

html=f.read()
print(html)