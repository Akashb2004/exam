import time
start = time.time()
class Node:
    def	__init__(self,data):
        self.data = data
        self.ref = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self,data):
        new_Node = Node(data)
        new_Node.ref = self.head
        self.head = new_Node
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete LL is empty !")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n==n.ref
        if n.ref is None:
            print("Node is not present !")
        else:
            n.ref=n.ref.ref
    def Search_value(self,x):
        if self.head is None:
            print("can't delete LL is empty !")
            return
        if x==self.head.data:
            self.head = self.head.ref
            print("Node is present at Beginning!")
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                print("Node is present!")
                break
            n==n.ref
L1 = Linkedlist ()
L1.add_begin (10)
L1.add_begin (20)
L1.add_begin (30)
L1.delete_by_value(20)
L1.print_LL()
L1.Search_value (10)
end = time.time()
print(f"Runtime of the program is {end - start}")
