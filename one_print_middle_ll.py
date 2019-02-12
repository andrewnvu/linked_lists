#print the middle of a linked list

class Node():
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def print(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next        
        cur_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # method 1
    # def printMiddle(self):
    #     two_nodes = self.head
    #     one_node = self.head

    #     while two_nodes.next:
    #         one_node = one_node.next
    #         two_nodes = two_nodes.next
    #         two_nodes = two_nodes.next

    #     print(one_node.data)

    #method 2
    def printMiddle(self):
        lead_node = self.head
        mid_node = self.head
        index = 0

        while lead_node.next:
            if index % 2  == 0:
                mid_node = mid_node.next

            lead_node = lead_node.next
            index += 1
        
        print(mid_node.data) 
        



myList = linkedList()
myList.append("A")
myList.append("B1")
myList.append("B2")
myList.append("B3")
myList.prepend("C")
myList.printMiddle()

myList.print()