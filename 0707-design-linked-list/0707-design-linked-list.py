class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0   # tracks length so we don't recompute it every time

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index > self.size:
            return                      # index too far out, do nothing
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        new_node = Node(val)
        temp = self.head
        for _ in range(index - 1):      # walk to the node BEFORE index
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):  # walk to the node BEFORE index
                temp = temp.next
            temp.next = temp.next.next
        self.size -= 1