def pairs(k, arr):
    # Write your code here
    count=0
    setter=set(arr)
    for i in arr:
        if(i-k in setter):
            count+=1
    return count