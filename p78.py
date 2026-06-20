# checking if matrix is symmetric or not
A=[[1,2],[2,1]]
symmetric=True
for i in range(2):
    for j in range(2):
        if A[i][j]!=A[j][i]:
            symmetric=False
            break
if symmetric:
    print("matrix is symmetric")
else:
    print("matrix is not symmetric")




