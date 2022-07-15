n=[1,3,4,5,6]
m=4
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==m:
            print(i+1,j+1)
