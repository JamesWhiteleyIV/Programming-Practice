# Queue via Stacks 
from data_structures.Stack import Stack

class My_Queue:
    ''' implementation of a queue using 2 stacks '''
    def __init__(self):
        ''' add: push everything to s1 first '''
        ''' remove: push everything to self.s2 first '''
        self.s1 = Stack()
        self.s2 = Stack()

    def __str__(self):
        return "s1:\n" + str(self.s1) + "\ns2:\n" + str(self.s2)

    def add(self, value):   
        while not self.s2.is_empty():
            self.s1.push(self.s2.pop())
        self.s1.push(value)
 
    def remove(self):   
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())
        self.s2.pop()

    def is_empty(self):
        return self.s1.data == [] and self.s2.data == []

    def size(self):
        return len(self.s1.data) + len(self.s2.data)

            

if __name__ == "__main__":
    q = My_Queue()
    print "adding 1, 2, 3"
    q.add(1)
    q.add(2)
    q.add(3)
    print q
    print "empty should == False"
    q.is_empty()
    print "size should == 3"
    q.size()
    print "removing 1"
    q.remove()
    print q
    print "adding 5"
    q.add(5)
    print q
    print "removing 2"
    q.remove()
    print q
    print "removing 3"
    q.remove()
    print q
    print "removing 5"
    q.remove()
    print q
    print "empty should == True"
    q.is_empty()
    print "size should == 0"
    q.size()
