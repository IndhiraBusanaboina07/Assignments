
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
