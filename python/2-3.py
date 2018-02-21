# Delete Middle Node 
# O(1)
import unittest
from data_structures.Linked_List import Linked_List


def del_middle(node):
    ''' deletes node '''
    if node is None or node.next is None:  
        return False #node is NULL or tail node

    node.data = node.next.data
    node.next = node.next.next
    return True


if __name__ == "__main__":
    print '---------Test 1-------------'
    ll = Linked_List()
    ll.add_front(1)
    ll.add_back(2)
    ll.add_back(3)
    ll.add_back(4)
    ll.add_back(5)
    ll.add_back(6)
    node = ll.head.next.next
    print ll
    print "calling del_middle on 3"
    print del_middle(node)
    print ll
    
