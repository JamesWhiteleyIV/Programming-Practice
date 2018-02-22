# Sort Stacks 
from data_structures.Stack import Stack

def compare(s1, s2):
    ''' helper function to order stack '''
    temp = s1.pop()

    if temp > s2.peek():
        s2.push(temp)
    else:
        while temp < s2.peek() and not s2.is_empty():
            s1.push(s2.pop())
        s2.push(temp)


def sort_stack(s1):
    ''' sorts a stack with smallest elements on top '''

    if s1.is_empty():
        return False

    s2 = Stack()
    s2.push(s1.pop())

    while not s1.is_empty():
        compare(s1, s2)

    while not s2.is_empty():
        s1.push(s2.pop())


if __name__ == "__main__":
    print "-------Test 1----------"
    print "unsorted stack test"
    s = Stack()
    s.push(4)
    s.push(1)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(5)
    s.push(1)
    print "INITIAL:"
    print s
    sort_stack(s)
    print "FINAL:"
    print s

    print "-------Test 2----------"
    print "already sorted stack test"
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    print "INITIAL:"
    print s
    sort_stack(s)
    print "FINAL:"
    print s


    print "-------Test 1----------"
    print "Empty stack test"
    s = Stack()
    print "INITIAL:"
    print s
    sort_stack(s)
    print "FINAL:"
    print s

