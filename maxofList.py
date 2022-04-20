def maxoflist(l):
    max=0
    for i in l:
        if(i>max):
            max=i
    return max

l=[1,2,3,4,5,6]
ans=maxoflist(l)
print(ans)
