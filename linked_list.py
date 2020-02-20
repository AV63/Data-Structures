
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def insert(self, data):
        newNode = Node(data)
        if self.start == None:
            self.start = newNode(data)
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
    def display(self):
        temp = self.start
        while temp.next != None:
            print(temp.data, end = " ")
            temp = temp.next
h = LinkedList()
h.insert(4)
h.display()


