class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
   
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_first(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_after(self, data, value):
        itr = self.head

        while itr.data != value:
            itr = itr.next
        itr.next = Node(data, itr.next)
        
    def Print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
        print()


if __name__ == '__main__':

    ll = LinkedList()

    ll.insert_at_first(5)
    ll.insert_at_first(4)
    ll.insert_at_first(3)
    ll.insert_at_first(2)
    ll.insert_at_first(1)
    ll.Print()

    ll.insert_at_last(2)
    ll.insert_at_last(3)
    ll.insert_at_last(1)
    ll.insert_at_last(4)
    ll.insert_at_last(5)
    ll.Print()

    ll.insert_after(10, 1)
    ll.Print()

# output
# 1 2 3 4 5
# 1 2 3 4 5 2 3 1 4 5
# 1 10 2 3 4 5 2 3 1 4 5