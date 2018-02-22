# Three in One 
import unittest

class Three_In_One:
    ''' implements three stacks using one fixed size array 
        stack 1 = [0 , n/3)
        stack 2 = [n/3, 2n/3)
        stack 3 = [2n/3, n)
    '''

    def __init__(self, size):
        ''' size = max size of each three arrays '''
        self.data = [None] * (size * 3)
        self.size = size * 3
        self.bounds = {  # min and max position in array of each stack
            1: {'minimum': 0, 'maximum': self.size / 3 - 1},
            2: {'minimum': self.size / 3, 'maximum': 2 * self.size / 3 - 1},
            3: {'minimum': 2 * self.size / 3, 'maximum': self.size - 1}
        }
        self.cur = {
            1: 0,
            2: self.size / 3,
            3: 2 * self.size / 3
        }

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            return False #stack already full
        else:
            pos = self.cur[stack_num]
            self.data[pos] = value
            self.cur[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            return False #stack already empty 
        else:
            pos = self.cur[stack_num] - 1
            self.data[pos] = None 
            self.cur[stack_num] -= 1

    def is_empty(self, stack_num):
        return self.data[self.bounds[stack_num]['minimum']] is None

    def is_full(self, stack_num):
        return self.data[self.bounds[stack_num]['maximum']] is not None

    def size(self, stack_num):
        return self.cur[stack_num] - self.bounds[stack_num]['minimum']

    def peek(self, stack_num):
        if not is_empty(stack_num):
            pos = self.cur[stack_num]
            return self.data[pos]

    def print_all(self):
        i = 0
        for item in self.data:
            print i, item 
            i += 1
        

if __name__ == "__main__":
    s = Three_In_One(5) 
    print 'pushing a, b, c, d to stack 2'
    s.push(2, 'a')
    s.push(2, 'b')
    s.push(2, 'c')
    s.push(2, 'd')
    s.print_all()
    print 'pushing q, p, r to stack 3'
    s.push(3, 'q')
    s.push(3, 'p')
    s.push(3, 'r')
    s.print_all()
    print 'popping stack 3'
    s.pop(3)
    s.print_all()
    print 'popping stack 3, 7x'
    s.pop(3)
    s.pop(3)
    s.pop(3)
    s.pop(3)
    s.pop(3)
    s.pop(3)
    s.pop(3)
    s.print_all()
    print 'pushing 1, 2, 3, 4, 5, 6 to stack 1'
    s.push(1, 1)
    s.push(1, 2)
    s.push(1, 3)
    s.push(1, 4)
    s.push(1, 5)
    s.push(1, 6)
    s.print_all()
    print 'popping stack 1, 2x'
    s.pop(1)
    s.pop(1)
    s.print_all()
