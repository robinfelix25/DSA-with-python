

"""
creating a singly linked list
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self, start):
        while start.next != None:
            print(start.value)
            start.next = start.next.next

sl = SlinkedList()
sl.head = Node(1)
sl.head.next = Node(2)
sl.tail = Node(2)