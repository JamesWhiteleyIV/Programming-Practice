class peg:
    def __init__(self, name, vals):
        self.vals = vals
        self.name = name
        

class Towers:
    ''' 
        Disk sizes are represented by ints, higher number = bigger disk.
        Position 0 is the top ex: [1, 2, 3]  1 on top of 2 on top of 3.
    '''

    def __init__(self, n):
        self.a = peg('a', [x+1 for x in range(n)])
        self.b = peg('b', [])
        self.c = peg('c', [])
        self.n = n  #number of total disks

    def _print(self):
        print "A: ", self.a.vals
        print "B: ", self.b.vals
        print "C: ", self.c.vals


    def move(self, t1, t2):
        ''' 
            moves top disk of t1 to top of tower t2.
            ex:  a = [1, 2, 3]  b = []
                 move(a, b)
                 a = [2, 3]  b = [1]
        '''
        disk = t1.vals.pop(0)
        t2.vals.insert(0, disk)

    def solve(self, n, start, goal, spare):
        ''' 
            Solves tower of hanoi algorithm moving all disks from a to c
            Trick: first call to solve swaps spare and goal
                   second call to solve swaps spare and start
                   simple as that :)
        '''
        if n <= 0:
            return

        if n == 1:
            self.move(start, goal)

        else:
            self.solve(n - 1, start, spare, goal)
            self.move(start, goal)
            self.solve(n - 1, spare, goal, start)


if __name__ == "__main__":
    n = 3 
    t = Towers(n)

    print "BEFORE:"
    t._print()
    t.solve(n, t.a, t.c, t.b)
    print "AFTER:"
    t._print()
   
