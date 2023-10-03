class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c

   def get(list,index):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        return n._value
   
   def set(list,index,value):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        n._value=value


def isPrime(n):
    flag = 0
    for i in range(2,int((n)/2+1)):
        if n%i==0:
            flag=1
    if flag == 0:
        return 1
    else:
        return 0

def findPrime(list):
    current = list._first
    previous = list._first
    while current._next:
        previous = current           
        current = current._next      
        data = current._value
        if(isPrime(data) and data!=1 and data!=0):
            print(data)      
l1 = LinkedList()
for i in range(10):
    l1.append(i)
findPrime(l1)
       
