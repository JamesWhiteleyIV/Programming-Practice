# kth to last 
# O(N) where N = length of linked list 
import unittest
from data_structures.Linked_List import Linked_List


def kth_to_last(k, ll):
    ''' returns kth to last node in Singly Linked List ll '''
    if ll.head is None:
        return None

    slow = fast = ll.head

    for _ in range(k):
        if fast is None:
            return None  # out of bounds
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    print '---------Test 1-------------'
    ll = Linked_List()
    ll.add_front(1)
    ll.add_back(2)
    ll.add_back(3)
    ll.add_back(4)
    ll.add_back(5)
    ll.add_back(6)
    print ll
    print "calling kth to last, k = 0 (invalid)"
    print kth_to_last(0, ll)
    print "calling kth to last, k = len(ll) (first)"
    print kth_to_last(len(ll), ll)
    print "calling kth to last, k = 1 (last)"
    print kth_to_last(1, ll)
    print "calling kth to last, k = 2 (second to last)"
    print kth_to_last(2, ll)
    print "calling kth to last, k = 10 (out of bounds)"
    print kth_to_last(10, ll)

