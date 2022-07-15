start=1
while(start!=10):
    f=open('abc.pdf','r')
    g=open(f"file{start}.pdf",'a')
    for i in f:
        g.write(i)
    start+=1