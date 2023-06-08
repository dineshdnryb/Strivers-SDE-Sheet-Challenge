# Coding Ninja
def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    ans=[[1]]
    for row in range(1,n):
        tempcol=[]
        for col in range(row+1):
            if(col-1<0 or col>row-1):
                tempcol.append(1)
            else:
                tempcol.append(ans[row-1][col-1]+ans[row-1][col])
        ans.append(tempcol)

    return ans