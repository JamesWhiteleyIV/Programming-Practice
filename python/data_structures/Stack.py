# Stack implementation

class Stack():
    def __init__(self):
        self.data = []

    def __iter__(self):
        for item in self.data:
            yield item

    def __str__(self):
        s = '------Top------\n' 
        for item in reversed(self.data):
            s += '\t' +  str(item) + '\n'
        s += '------Bottom------'
        return s

    def __len__(self):
        return self.size()

    # O(1)
    def push(self, item):
        self.data.append(item)

    # O(1)
    def pop(self):
        return self.data.pop()

    # O(1)
    def is_empty(self):
        return self.data == [] 

    # O(1)
    def size(self):
        return len(self.data)

    # O(1)
    def peek(self):
        return self.data[self.size() - 1]


if __name__ == "__main__":
	print "TESTING STACK"
	s = Stack()
	print "pushing 1, 2, 3"
	s.push(1)
	s.push(2)
	s.push(3)    
	print "size should == 3"
	print s.size()
	print len(s)
	print "popping top"
	s.pop()
	print "size should == 2"
	print s.size()
	print "is empty should be False"
	print s.is_empty()
	print "should print 2 and 1"
	print s
	print "popping top"
	s.pop()
	print "popping top"
	s.pop()
	print "size should == 0"
	print s.size()
	print "is empty should be True"
	print s.is_empty()
