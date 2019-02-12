#Rotating a SINGLY linked list counter-clockwise by a number k 
#i.e. 10 - 20 - 30 -40 - 50 -60 - NULL
# k is 4
# 50 - 60 - 10 - 20 - 30 -40 - NULL
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def rotate(self,k):
        old_head = self.head
        current_node = self.head
        for _ in range (k-1):
            current_node = current_node.next
        self.head = current_node.next
        current_node.next = None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = old_head
    





myList = linkedList()
myList.append(10)
myList.append(20)
myList.append(30)
myList.append(40)
myList.append(50)
myList.append(60)
myList.rotate(4)
myList.print()