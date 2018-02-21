# Remove Duplicates
import unittest
from data_structures.Linked_List import Linked_List

# O(N)
def remove_dups(ll):
    ''' removes all duplicates from unsorted Singly Linked List ll '''
    if ll.head is None:
        return

    cur = ll.head
    d = {cur.data: True}
    while cur.next:
        if cur.next.data in d:
            cur.next = cur.next.next
        else:
            d[cur.next.data] = True
            cur = cur.next


# O(N^2)
def remove_dups_no_buff(ll):
    ''' removes all duplicates from unsorted Singly Linked List ll without using temporary buffer '''
    if ll.head is None:
        return

    slow = fast = ll.head
    while slow:
        while fast.next:
            if slow.data == fast.next.data:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = fast = slow.next


if __name__ == "__main__":
    print '---------Test 1-------------'
    ll = Linked_List()
    ll.add_front(4)
    ll.add_back(5)
    ll.add_back(6)
    ll.add_back(6)
    ll.add_back(7)
    ll.add_back(6)
    print ll
    print "calling remove dups"
    remove_dups(ll)
    print ll
    print '---------Test 2-------------'
    ll = Linked_List()
    ll.add_front(4)
    ll.add_back(5)
    ll.add_back(6)
    ll.add_back(6)
    ll.add_back(7)
    ll.add_back(6)
    print ll
    print "calling remove dups no buff"
    remove_dups_no_buff(ll)
    print ll
    print '---------Test 3-------------'
    ll = Linked_List()
    print "empty ll:", ll
    print "calling remove dups no buff"
    remove_dups_no_buff(ll)
    print "empty ll:", ll

