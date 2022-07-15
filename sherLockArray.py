arr=[5,6,8,11]
suml=sum(arr[:0])
sumr=sum(arr[1:])
# # for i in range(len(arr)):
# #     suml=sum(arr[])
# # idx=0
# # n=len(arr)
# # print(n)
# # sumr=sum(arr[idx+1:n])
print(sumr)
# # suml=sum(arr[0:idx])
print(suml)
#//////////////////////////////////////////////////////
def balancedSums(arr):
    # Write your code here
    suml=sum(arr[:0])
    sumr=sum(arr[1:])
    if(suml==sumr):
        return "YES"
    for i in range (1,len(arr)):
        if(suml==sumr):
            return "YES"
        if(suml!=sumr):
            suml+=arr[i-1]
            sumr-=arr[i]
    return "NO"  

