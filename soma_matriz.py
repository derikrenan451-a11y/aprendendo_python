A =[
    [1,2],
    [3,4]
]

B=[
    [5,6],
    [7,8]
]

resultado_soma =[[0,0],[0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        resultado_soma[i][j] =A[i][j] +B[i][j]
        print(resultado_soma)  