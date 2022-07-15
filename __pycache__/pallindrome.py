name=input("enter the string to check its pallindrome or not")
j=len(name)-1
counter=0
for i in range(len(name)//2):
    if(name[i]==name[j]):
        j-=1
        counter+=1
if(counter==len(name)//2):
    print("Pallindrome")
else:
    print("Non Pallindrome")

    
