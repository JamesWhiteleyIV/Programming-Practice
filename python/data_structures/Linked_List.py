# Singly Linked List implementation

class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data 
        self.next = next_node 
        self.prev = prev_node 

    def __str__(self):
        return str(self.data)
        
        
class Linked_List:
    ''' singly-linked list implementation '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __str__(self):
        data = [str(x) for x in self]
        return ' -> '.join(data)

    def __len__(self):
        total = 0
        cur = self.head
        while cur:
            total += 1
            cur = cur.next
        return total
        
    def add_front(self, value):
        if self.head is None: # 0 nodes
            self.head = self.tail = Node(value)
        else:
            node = Node(value, next_node=self.head)
            self.head = node

    def remove_front(self):
        if self.head == self.tail:
            self.head = self.tail = None
        elif self.head:
            self.head = self.head.next

    def add_back(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            temp = self.tail
            self.tail = Node(value)
            temp.next = self.tail 

    def remove_back(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None
            self.tail = cur

    def remove_node(self, node):
        ''' removes node and returns node after removed node '''
        cur = self.head
        while cur:
            if cur.next == node:
                cur.next = cur.next.next
            cur = cur.next
        return cur

    def gen(self, *args):
        for arg in args:
            self.add_back(arg)
       

if __name__ == "__main__":
    print "TESTING SINGLY LINKED LIST"
    print "--------------------------"
    ll = Linked_List()
    ll.add_front(1)
    ll.add_front(2)
    print "Expected: 2->1"
    print ll
    ll.remove_front()
    print "Expected: 1"
    print ll
    ll.add_front(3)
    print "Expected: 3->1"
    print ll
    ll.add_back(2)
    print "Expected: 3->1->2"
    print ll
    ll.remove_back()
    print "Expected: 3->1"
    print ll
    print 'Expected: 2'
    print "length: ", len(ll)
    ll.remove_front()
    ll.remove_front()
    ll.remove_front()
    ll.remove_front()
    ll.remove_back()
    ll.remove_back()
    ll.remove_back()
    ll.remove_back()
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)
    ll.add_back(6)
    ll.add_back(7)
    ll.add_back(8)
    print "Expected: 1->2->3->4->5->6->7->8"
    print ll
    print "8 length: ", len(ll)
    ll.remove_front()
    print "Expected: 2->3->4->5->6->7->8"
    print ll
    print "7 length: ", len(ll)
    ll.remove_back()
    print "Expected: 2->3->4->5->6->7"
    print ll
    print "6 length: ", len(ll)
    ll.remove_front()
    print "Expected: 3->4->5->6->7"
    print ll
    print "5 length: ", len(ll)
    ll.remove_back()
    print "Expected: 3->4->5->6"
    print ll
    print "4 length: ", len(ll)
    for node in ll:
        if node.data == 5:
            ll.remove_node(node)
    print "Expected: 3->4->6"
    print ll
    print "3 length: ", len(ll)
    ll.remove_back()
    ll.remove_back()
    ll.remove_back()
    ll.remove_back()
    print ll
    print "0 length: ", len(ll)



