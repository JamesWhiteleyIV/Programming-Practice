# Queue implementation

class Queue:
    def __init__(self):
        self.data = []

    def __iter__(self):
        for item in self.data:
            yield item

    def __str__(self):
        s = '------Front------\n' 
        for item in self:
            s += '\t' +  str(item) + '\n'
        s += '------Rear------'
        return s

    def __len__(self):
        return self.size()

    # O(1)
    def add(self, item):
        self.data.append(item)

    # O(N) has to shift all elements
    def remove(self):
        return self.data.pop(0)

    # O(1)
    def is_empty(self):
        return self.data == [] 

    # O(1)
    def size(self):
        return len(self.data)


if __name__ == "__main__":
    print "TESTING QUEUE"
    q = Queue()
    print "adding 1, 2, 3"
    q.add(1)
    q.add(2)
    q.add(3)    
    print "size should == 3"
    print q.size()
    print len(q)
    print "removing front"
    q.remove()
    print "size should == 2"
    print q.size()
    print "is empty should be False"
    print q.is_empty()
    print "should print 2 and 3"
    print q
    print "removing front"
    q.remove()
    print "removing front"
    q.remove()
    print "size should == 0"
    print q.size()
    print "is empty should be True"
    print q.is_empty()
