class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linkedlist:
    head=node()

    def display(self):
        if self.head is None:
            print("-1")
        start=self.head
        while(start!=None):
            print(start.data)
            start=start.next

    def isEmpty(self):
        return self.head==None

    def insertBeg(self,data):
        newnode=node(data)
        if(self.isEmpty()):
             self.head=newnode
        newnode.next=self.head
        self.head=newnode
    
    def deleteBeg(self):
        if(self.isEmpty()):
            return -1
        x=self.head.data
        self.head=self.head.next
        return x

obj=node(5)
object=linkedlist()
object.head=obj
object.insertBeg(23)
object.insertBeg(24)
object.insertBeg(25)
object.insertBeg(26)
object.insertBeg(27)
# print(object)
object.display()
object.deleteBeg()
object.deleteBeg()
object.deleteBeg()
object.deleteBeg()
object.deleteBeg()
object.deleteBeg()
object.deleteBeg()
object.display()
    
