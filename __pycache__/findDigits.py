n=110110015
temp=n
l=[]
while(temp!=0):
    l.append(temp%10)
    temp=temp//10
print(l)
count=0
k=0
while k in l:
    l.remove(k)
for i in l:
    if(n%i==0):
        count+=1
print(count)