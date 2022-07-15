d={}
z=97
h=[1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
for i in h:
    d.update({chr(z):i})
    z+=1
w="torn"
r=len(w)
# print(r)
# print(d)
l=[]
for i in w:
    if i in d.keys():
        l.append(d.get(i))
print(max(l)*r)