arr=[7,2,5,3,5,3,1]
brr=[7,2,5,4,6,3,5,3,1,1]
# print(brr.count(1))
ar=list(set(arr))
br=list(set(brr))
for i in br:#originalArray
    if((i not in ar) or (arr.count(i)!=brr.count(i))):
        print(i)