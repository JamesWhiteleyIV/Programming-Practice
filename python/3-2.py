# Stack Min 
# implementation of stack with min function that takes O(1) time and returns minimum 
from data_structures.Stack import Stack

class Stack_Min(Stack):
    def __init__(self):
        self.data = []
        self.min = [] 

    # O(1)
    def push(self, item):
        self.data.append(item)
        if self.min == []:
            self.min.append(item)
        elif item <= self.min[-1]:
            self.min.append(item)

    # O(1)
    def pop(self):
        if self.data[-1] == self.min[-1]:
            self.min.pop()
        return self.data.pop()

    # O(1)
    def min_val(self):
        if not self.is_empty():
            return self.min[-1]

    def print_min_list(self):
        s = '------Top------\n' 
        for item in reversed(self.min):
            s += '\t' +  str(item) + '\n'
        s += '------Bottom------'
        print s



if __name__ == "__main__":
    s = Stack_Min()
    s.push(9)
    s.push(10)
    s.push(11)
    s.push(8)
    s.push(7)
    print s
    print s.min_val()
    s.pop()
    print s
    print s.min_val()
    s.pop()
    print s
    print s.min_val()
    s.pop()
    print s
    print s.min_val()
    s.push(1)
    s.push(2)
    s.push(1)
    print s
    print s.min_val()
    s.pop()
    print s
    print s.min_val()
