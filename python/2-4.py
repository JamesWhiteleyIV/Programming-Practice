# Partition 
# O(N) where N = # of nodes in Linked List
import unittest
from data_structures.Linked_List import Linked_List


def partition(ll, val):
    ''' changes linked list ll to have all values < val on left of all values >= val '''
    if ll.head is None: # no nodes
        return False 

    if ll.head.next is None: # 1 node
        return False

    # create 2 linked lists that contain values >= or < val
    gte_ll = Linked_List() 
    lt_ll = Linked_List()
    cur = ll.head

    while cur:
        if cur.data >= val:
            gte_ll.add_front(cur.data)
        else:
            lt_ll.add_front(cur.data)
        cur = cur.next

    # combine linked lists
    if lt_ll.tail is not None:
        lt_ll.tail.next = gte_ll.head
        ll.head = lt_ll.head
    return True


if __name__ == "__main__":
    print '---------Test 1-------------'
    ll = Linked_List()
    ll.add_front(1)
    ll.add_back(2)
    ll.add_back(4)
    ll.add_back(9)
    ll.add_back(5)
    ll.add_back(3)
    ll.add_back(6)
    ll.add_back(2)
    ll.add_back(2)
    print ll
    print "calling partition, val = 4"
    print partition(ll, 4)
    print ll

    print '---------Test 2-------------'
    print 'all nodes < val'
    ll = Linked_List()
    ll.add_front(5)
    ll.add_back(2)
    ll.add_back(4)
    ll.add_back(9)
    ll.add_back(5)
    ll.add_back(3)
    ll.add_back(6)
    ll.add_back(2)
    ll.add_back(2)
    print ll
    print "calling partition, val = 30"
    print partition(ll, 30)
    print ll   

    print '---------Test 3-------------'
    print 'all nodes >= val'
    ll = Linked_List()
    ll.add_front(5)
    ll.add_back(2)
    ll.add_back(4)
    ll.add_back(9)
    ll.add_back(5)
    ll.add_back(3)
    ll.add_back(6)
    ll.add_back(2)
    ll.add_back(2)
    print ll
    print "calling partition, val = 1"
    print partition(ll, 1)
    print ll   
