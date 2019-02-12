class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList():
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        
        cur_node.next = new_node

    def print(self):
        if self.head == None:
            return print(None)
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def removeMiddle(self):
        tail_node = self.head
        mid_node = self.head
        index = 0
        mid_index = 0
        while tail_node.next:
            if index % 2 == 0: 
                mid_node = mid_node.next
                mid_index +=1
                print(mid_index, "mid")
            tail_node = tail_node.next
            index += 1
        print(index)
        cur_node = self.head
        for _ in range (mid_index -1):
            cur_node = cur_node.next
        cur_node.next = mid_node.next
        del mid_node



myList = linkedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
myList.print()
myList.removeMiddle()
myList.print()