t=int(input())
i=1
while i <= t:
    i+=1
    h,m=map(int,input().split())
    hour=h*30+30*m/60
    min=m*6
    ang=hour-min
    if ang<0:
        ang*=-1
    if ang>180:
        ang=360-ang
    print(int(ang))

