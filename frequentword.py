def freqcount(str,makeset):
    dictionary={}
    for i in makeset:
        r=str.count(i)
        dictionary.update({i:r})
    new_value=max(dictionary,key=dictionary.get)
    print(new_value)
    print(dictionary.get(new_value))
    pass
#Driver Code
str="hello hello hello how are how you"
makeset=set(list(str.split(" ")))
# print(makeset)
freqcount(str,makeset)