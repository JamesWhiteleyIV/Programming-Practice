# Stack of Plates 
from data_structures.Stack import Stack

class Set_Of_Stacks:
    ''' once a stack reaches the threshold, a new stack is created '''
    def __init__(self, threshold):
        self.threshold = threshold
        self.data = {
            1: Stack()
        }
        self.cur = 1 #current stack

    def __str__(self):
        s = ""
        for key in self.data:
            s += "\nStack {}\n".format(key)
            s += '------Top------\n' 
            for item in reversed(self.data[key].data):
                s += '\t' +  str(item) + '\n'
            s += '------Bottom------'
        return s

    def is_full(self, stack):
        return len(stack) == self.threshold

    def is_empty(self, stack):
        return len(stack) == 0 

    def push(self, item):
        if self.is_full(self.data[self.cur]):
            self.cur += 1
            if self.cur not in self.data:
                self.data[self.cur] = Stack()
        self.data[self.cur].push(item)

    def pop(self):
        if self.is_empty(self.data[self.cur]):
            if self.cur is not 1:
                self.cur -= 1
        self.data[self.cur].pop()


if __name__ == "__main__":
    s = Set_Of_Stacks(3)
    print "pushing 1, 2, 3, 4"
    s.push(1)
    s.push(2)
    s.push(3)    
    s.push(4)    
    print s
    print "popping top"
    s.pop()
    print s
    print "pushing a, b, c, d, e, f, g"
    s.push('a')
    s.push('b')
    s.push('c')
    s.push('d')
    s.push('e')
    s.push('f')
    s.push('g')
    print s

