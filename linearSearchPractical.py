from re import I


def Lsearch(arr,key):
    for i in arr:
        if i==key:
            return arr.index(i)
    else:
        return -1
arr=[3,45,67,89,12]
key=899
print(Lsearch(arr,key))