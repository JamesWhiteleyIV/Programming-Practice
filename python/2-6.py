# Palindrome 
# O(N) where N = # nodes in linked list
import unittest
from data_structures.Linked_List import Linked_List

def palindrome(ll):
    ''' returns True if linked list ll is a palindrome (same forward and backwards) '''
    if ll.head is None:
        return False

    cur = ll.head
    string = []

    while cur:
        string.append(cur.data)
        cur = cur.next

    string = ''.join(string)
    rev = string[::-1]

    return string == rev


def alt_palindrome(ll):
    ''' returns True if linked list ll is a palindrome (same forward and backwards) '''
    if ll.head is None:
        return False

    stack = []
    fast = slow = ll.head

    #fast will reach the end when slow is in the middle
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if stack.pop() != slow.data:
            return False
        
        slow = slow.next

    return True


class Test(unittest.TestCase):
    data  = (
        (('k', 'a', 'y', 'a', 'k'), True),
        (('k', 'a', 'y', 'y', 'k'), False),
        (('k'), True),
        (('k', 'k', 'a'), False),
        (('k', 'a'), False),
        ((), False),
    )
    
    def test_func(self):
        for [nodes, expected] in self.data:
            ll = Linked_List()
            ll.gen(*nodes)
            self.assertEqual(palindrome(ll), expected)

    def test_alt_func(self):
        for [nodes, expected] in self.data:
            ll = Linked_List()
            ll.gen(*nodes)
            self.assertEqual(alt_palindrome(ll), expected)


if __name__ == "__main__":
    unittest.main()
