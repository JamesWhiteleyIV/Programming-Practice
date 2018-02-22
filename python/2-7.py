# Intersect 
# O(N + M) where N and M  = # nodes in Linked Lists
# Brute force would be O(NM) where N and M are the number of nodes in each LL
import unittest
from data_structures.Linked_List import Linked_List
from data_structures.Linked_List import Node 

def intersect(ll1, ll2):
    ''' returns the intersecting node if exists, else return None '''
    if ll1.head is None or ll2.head is None:
        return None

    d = {}
    cur = ll1.head

    while cur:
        d[cur] = True
        cur = cur.next

    cur = ll2.head
    while cur:
        if cur in d:
            return cur
        cur = cur.next

    return None


if __name__ == "__main__":
    print "--------------Test 1--------------"
    ll1 = Linked_List()
    ll2 = Linked_List()

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')

    ll1.head = a
    a.next = b
    b.next = c
    c.next = e
    ll1.tail = e 
    # a -> b -> c - > e

    ll2.head = d
    d.next = c 
    ll2.tail = c 
    #  d -> c

    print ll1
    print ll2

    print "has intersection = ", intersect(ll1, ll2)
    print ""

    print "--------------Test 2--------------"
    ll1 = Linked_List()
    ll2 = Linked_List()

    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    p = Node('p')

    ll1.head = a
    a.next = b
    b.next = c
    c.next = e
    ll1.tail = e 
    # a -> b -> c - > e

    ll2.head = d
    d.next = p 
    ll2.tail = p 
    #  d -> p 

    print ll1
    print ll2

    print "has intersection = ", intersect(ll1, ll2)

