lst=[[1,2],[4,5],[6,7]]
def solution(mat):
    mat_ret=[]
    for i in range(len(mat[0])): #[1,2]=2
        mat_ret.append(0) #[0,0]  기본 리스트를 만들어줌
    for i in range(len(mat)): #len=3
        for j in range(len(mat[0])): #len=2 0~1
            mat_ret[j]+=mat[i][j] #mat_ret[j]=int 알아서 리스트에 쌓임 ->mat_ret[]번째가 새롭게 정의되는 거임

    return mat_ret
print(solution(lst))

