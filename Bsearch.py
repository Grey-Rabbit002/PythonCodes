def bsearch(arr,beg,end,key):
    if(beg<end):
        mid=(beg+end) //2
        if arr[mid]==key:
            return mid
        elif(arr[mid]>key):
            return bsearch(arr,beg,mid-1,key)
        elif arr[mid]<key:
            return bsearch(arr,mid+1,end,key)
    else:
        return -1

arr=[1,2,3,6,9,12,22]
key=6
r=bsearch(arr,0,len(arr),36)
print("index at which value is present",r)