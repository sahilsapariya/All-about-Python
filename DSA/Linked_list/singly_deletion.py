class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class linkedlist:
    def __init__(self):
        self.head = None

    def delete_at_first(self):
        itr = self.head
        self.head = itr.next
        
        del itr

    def delete(self, value):
        if self.head == None:
            print("Linked list is empty.")
            return
        itr = self.head
        while itr.next.data != value:
            itr = itr.next
        itr.next = itr.next.next

    
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
    
    ll = linkedlist()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    ll.Print()

    ll.delete(3)
    ll.Print()

    ll.delete_at_first()
    ll.Print()

# output
# 1 2 3 4 5
# 1 2 4 5
# 2 4 5