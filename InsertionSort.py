def Insertion(arr,n):
    for i in range(1,n,1):
        key=arr[i]
        j=i-1
        while j>-1 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
a=[1,3,2,9,5,6]
Insertion(a,len(a))
print(a)