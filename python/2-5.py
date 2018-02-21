# Sum Lists 
# O(N) where N = # of nodes in bigger Linked List
import unittest
from data_structures.Linked_List import Linked_List


# oops! read the questions wrong needed to output linked list
def sum_lists(ll1, ll2):
    ''' sums two linked lists
    ex:
        ll1 = 7 -> 1 -> 6   (617)
        ll2 = 5 -> 9 -> 2   (295)
        result = 617 + 295 = 912
    '''
    result = 0
    multiple = 1

    if len(ll1) > len(ll2):
        big = ll1.head
        small = ll2.head
    else:
        big = ll2.head
        small = ll1.head

    while big:
        if small:
            result += (big.data + small.data) * multiple
            small = small.next
        else:
            result += big.data * multiple
        multiple *= 10
        big = big.next

    return result


# take two!
def sum_lists_tt(ll1, ll2):
    ''' sums two linked lists
    ex:
        ll1 = 7 -> 1 -> 6   (617)
        ll2 = 5 -> 9 -> 2   (295)
        result = 617 + 295 = 912 =  2 -> 1 -> 9 
    '''
    result = Linked_List() 
    carry = 0

    if len(ll1) > len(ll2):
        big = ll1.head
        small = ll2.head
    else:
        big = ll2.head
        small = ll1.head

    while big:
        if small:
            num = big.data + small.data + carry
            small = small.next
        else:
            num = big.data + carry
            
        if num < 10: # no double digit, no carry
            carry = 0 
        else:
            carry = 1
            num %= 10 #get digit in one's place

        big = big.next
        result.add_back(num)

    return result


# This doesn't work but i'm moving on.
def forward_sum_lists(ll1, ll2):
    ''' sums two linked lists
    ex:
        ll1 = 6 -> 1 -> 7   (617)
        ll2 = 2 -> 9 -> 5   (295)
        result = 617 + 295 = 912
        output = 9 -> 1 -> 2
    '''
    result = Linked_List() 
    carry = 0
    last = None 

    if len(ll1) > len(ll2):
        big = ll1
        small = ll2
    else:
        big = ll2
        small = ll1

    # 0 pad the small linked list to make same # nodes
    for _ in range ( len(big) - len(small) ):
        small.add_front(0)

    big = big.head
    small = small.head

    while big:
        val = big.data + small.data

        #no need to add a carry
        if val < 10 and last is not None:
            result.add_back(last)
            last = val
        elif last is not None: #val >= 10
            result.add_back(last + 1) #add the carry
            last = val % 10 
        else:
            last = val 

        big = big.next
        small = small.next

    return result





if __name__ == "__main__":
    print '---------Test 1-------------'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling sum_lists()"
    print sum_lists(ll1, ll2)

    print '---------Test 2-------------'
    print 'One empty list'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    print ll1
    print ll2
    print "calling sum_lists()"
    print sum_lists(ll1, ll2)

    print '---------Test 3-------------'
    print 'different size lists'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling sum_lists()"
    print sum_lists(ll1, ll2)

    print '---------Test 1-------------'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling sum_lists_tt()"
    print sum_lists_tt(ll1, ll2)

    print '---------Test 2-------------'
    print 'One empty list'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    print ll1
    print ll2
    print "calling sum_lists_tt()"
    print sum_lists_tt(ll1, ll2)

    print '---------Test 3-------------'
    print 'different size lists'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling sum_lists_tt()"
    print sum_lists_tt(ll1, ll2)

    print '---------Test 1-------------'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling forward_sum_lists()"
    print forward_sum_lists(ll1, ll2)

    print '---------Test 2-------------'
    print 'One empty list'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll1.add_back(6)
    ll2 = Linked_List()
    print ll1
    print ll2
    print "calling forward_sum_lists()"
    print forward_sum_lists(ll1, ll2)

    print '---------Test 3-------------'
    print 'different size lists'
    ll1 = Linked_List()
    ll1.add_back(7)
    ll1.add_back(1)
    ll2 = Linked_List()
    ll2.add_back(5)
    ll2.add_back(9)
    ll2.add_back(2)
    print ll1
    print ll2
    print "calling forward_sum_lists()"
    print forward_sum_lists(ll1, ll2)

