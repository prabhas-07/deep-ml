def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if(len(a[0])!=len(b)):
        return -1
    ans=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            sum=0
            for k in range(len(b)):
                sum+=a[i][k]*b[k][j]
            row.append(sum)
        ans.append(row)


    return ans