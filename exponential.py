def expo(a,n):
    if(n==0):
        return 1
    return a * expo(a,n-1)
    pass

a=2
n=5
ans=expo(a,n)
print(ans)