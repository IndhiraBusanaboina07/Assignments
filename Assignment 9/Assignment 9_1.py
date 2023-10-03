class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous


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

       