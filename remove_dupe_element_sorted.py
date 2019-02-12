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
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def removeDupes(self):
        cur_node = self.head
        n_node = cur_node.next

        while cur_node.next:
            prev_node = n_node
            if cur_node.data == n_node.data:
                n_node = n_node.next
                cur_node.next = n_node
                del prev_node
            else:
                cur_node = cur_node.next
                n_node = n_node.next

myList = linkedList()
myList.append(11)
myList.append(11)
myList.append(11)
myList.append(21)
myList.append(43)
myList.append(60)
myList.print()
myList.removeDupes()
print("after removing dupes")
myList.print()
