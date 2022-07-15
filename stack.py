class stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    

s=stack()
while True:
    choice=int(input('enter choice as 1,2,3,4 for push pop and display and quit'))
    if(choice==1):
        value=int(input("enter value to be pushed"))
        s.push(value)
    elif(choice==2):
        if(s.is_empty()):
            print("empty stack")
        else:
            print("popped value is ",s.pop())
    elif(choice==3):
        if(s.is_empty()):
            print("empty stack")
        else:
            while(s.is_empty()!=True):
                print("  ",s.pop())
    elif(choice==4):
        break
    else:
        print("wrong chioice")


     