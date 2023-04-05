

"""
My own implemented of Singly linked list not sure its bug free :-)
revisit
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    
class SLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def printll(self, start):
        while start != None:
            print(str(start.value) , end="->")
            start = start.next
    
    def insertstart(self, value):
        if self.head:
            newnode = Node(value)
            newnode.next = self.head.next
            self.head = newnode
        else:
            newnode = Node(value)
            self.head = newnode
            self.tail = newnode

    def insertend(self, value):
        if self.tail:
            newnode = Node(value)
            self.tail.next = newnode
            self.tail = newnode
        else:
            newnode = Node(value)
            self.head = newnode
            self.tail =newnode

    def insertmiddle(self, value, position):
        curr = self.head
        i = 0
        if not self.head:
            self.insertstart(value)
            return 
        
        while i < position - 1:
            if curr is None:
                print('positon not available')
                return 
            curr = curr.next
            i += 1
        
        newnode = Node(value)
        newnode.next = curr.next
        curr.next = newnode


sl = SLinkedList()
sl.insertstart(1)
sl.insertend(2)
sl.insertend(3)
sl.insertmiddle(4,3)
sl.printll(sl.head)


