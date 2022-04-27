l=list(input("enter the list space seperted").split())
value="4"
for i in l:
    print(i)
    if(i==value):
        print("found")
        break
else:
    print("not found")