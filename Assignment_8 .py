
class Node:
    def _init_(self,data):
        self.data=data
        self.nextnode=None
class LinkedList:
    def _init_(self):
        self.head=None
        self.size=0
        self.tail = None
        self.nodebeforetail = None

    def insert_at_start(self,data):
        newnode=Node(data)
        self.size+=1
        if not self.head:
            self.head=newnode
        else:
            newnode.nextnode=self.head
            self.head=newnode

    def remove_last(self):
        if self.head is None:
            return None 
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        current = self.head
        while current.nextnode != self.tail:
            current = current.nextnode
        removed_data = self.tail.data
        current.nextnode = None
        self.tail = current
        return removed_data
            
            
          
    def size(self):
        return self.size

    def append(self,data):
        temp=self.head
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail = newnode
            self.size+=1
            print(f"Appended {self.tail.data}")
        else:
           
            self.tail.nextnode = newnode
            self.tail=newnode
            self.size+=1
            print(f"Appended {self.tail.data}")

    def count(self,value):
        temp=self.head
        count=0
        while(temp!=None ):
            if temp.data==value:
                count+=1
            temp=temp.nextnode
        return count
    
    def print_info(self):
        if self.head==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self.head
        while n:
            str+=f'{n.data}\t'
            n=n.nextnode
        str+=")"
        print(str)
        
ll = LinkedList()
ll.append(10)
ll.append(10)
ll.append(11)
ll.append(12)

ll.print_info()

size=ll.sizee()
print(f'The size of linked list is {size}')

ll.print_info()
print(f"size {ll.sizee()}")