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
def test():
 linked_list_1 = LinkedList()
 linked_list_2 = LinkedList()

 linked_list_1.append(1)
 linked_list_1.append(2)
 linked_list_2.append(3)
 linked_list_2.append(4)
