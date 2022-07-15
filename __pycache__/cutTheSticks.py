arr=[5,4,4,2,2,8]
l=[]
k=0
for i in range(len(arr)):
    mini=min(arr)
    arr[i]-=mini
    for j in range(len(arr)):
        if(arr[j]==0):
            arr.remove(arr[j])
    print(arr[i])
l.append(len(arr))
print(l)
    