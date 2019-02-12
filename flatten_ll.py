# Given a linked list where every node represents a linked list and contains two pointers of its type:
# (i) Pointer to next node in the main list (we call it ‘right’ pointer in below code)
# (ii) Pointer to a linked list where this node is head (we call it ‘down’ pointer in below code).

class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class linkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.right:
            cur_node = cur_node.right

        cur_node.right = new_node
    
    def appendDown(self, value, index):
        new_node = Node(value)

        if self.head == None:
            print("Got Nothing to append to, please use append()")
            return
        
        # counter = 0
        cur_node = self.head
        # while counter < index:
        #     cur_node = cur_node.right
        #     index +=1
        for _ in range(index):
            cur_node = cur_node.right

        while cur_node.down:
            cur_node = cur_node.down

        cur_node.down = new_node

    def printMain(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.right

    def printChilds(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.down
    
    def printAll(self):
        main_node = self.head
        cur_node = self.head
        while main_node:
            print(cur_node.data, "->",end = " ")
            cur_node = cur_node.down
            if cur_node == None:
                main_node = main_node.right
                cur_node = main_node
        print("NULL")

    def flatten(self):
        main_node = self.head
        cur_node = self.head
        while main_node:
            while cur_node is not None:
                cur_node.right = cur_node.down
                cur_node = cur_node.right
                if cur_node == None:
                    main_node = main_node.right
                    cur_node.right = main_node
                    cur_node = main_node
        
        

            

myList = linkedList()
myList.append(5)
myList.append(10)
myList.append(19)
myList.append(28)
myList.appendDown(35,3)
myList.appendDown(40,3)
myList.appendDown(45,3)
myList.appendDown(20,1)
myList.appendDown(50,2)
myList.appendDown(7,0)
myList.appendDown(8,0)
myList.appendDown(30,0)
myList.appendDown(22,2)
# myList.printMain()
# myList.printChilds()
myList.flatten()
myList.printMain()
