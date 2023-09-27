class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def isValidPos(self, pos):
        
        return (pos<=self.size)
    def insert(self, val, pos):
        
        
        if(self.size == 0 and pos == 1):
            new_node = Node(val)
            self.head = new_node
        
        print(self.isValidPos(pos))
        elif(isValidPos(pos) == False):
            print(self.isValidPos(pos))
            print("checked")
            return "Invalid Position"
        
        else: 
            
            
            ref = self.head
            count = 1
            
            while(count != pos):
                ref = ref.next
                count += 1
            
            new_node = Node(val)
            new_node.next = ref.next
            ref.next = new_node
        
        self.size += 1    
                   
def test():
 linked_list_1 = LinkedList()
 linked_list_2 = LinkedList()

 linked_list_1.append(1)
 linked_list_1.append(2)
 linked_list_2.append(3)
 linked_list_2.append(4)
