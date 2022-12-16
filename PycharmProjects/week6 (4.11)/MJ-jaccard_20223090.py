allSet=[{1,2,3,4,5,6,7,8,9,10}, {1,3,5,7,12,15}, {3,12,15,18,20}, {12,13,14,15,16,17,18,19}]

for i in range(1,4): #1,2,3
    J=len(allSet[0]&allSet[i])/len(allSet[0]|allSet[i])
    print(f"J(0,{i})",end='')
    print(J)
for i in range(2,4): #2,3
    J=len(allSet[1]&allSet[i])/len(allSet[1]|allSet[i])
    print(f"J(1,{i})", end='')
    print(J)
for i in range(3,4): #3
    J=len(allSet[2]&allSet[i])/len(allSet[2]|allSet[i])
    print(f"J(2,{i})", end='')
    print(J)



