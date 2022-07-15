sales=[12,12,12,12,11,11,45]
l=list(set(sales))
i=0
j=0
count=[]
for i in range(len(l)):
    # print(sales.count(l[i]))
    count.append(sales.count(l[i]))
print(count)
counter=0
for i in count:
    if(i/2 >=1):
        counter+=i//2
print("pair of socks are    ",counter)