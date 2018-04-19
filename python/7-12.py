
class Hash_Table:
    def __init__(self, size):
        self.size = size 
        self.table = [ [] for x in range(self.size) ]

    def _hash(self, key):
        ''' computes table index for key, val insertion '''
        _sum = 0
        key = str(key)

        for i in range(len(key)):
            _sum = _sum + ((i+1) * ord(key[i]))

        return _sum % self.size

    def show(self):
        ''' displays hash table idx by idx '''
        print '-------------------------'
        for i in range(self.size):
            print i, ':', self.table[i]


    def insert(self, key, val):
        ''' 
            inserts key, val pair in table. 
            updates if key exists already
        '''
        idx = self._hash(key)

        # check if key already exists
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx][i][1] = val #update value 
                return

        # d.n.e. so append 
        self.table[idx].append([key, val])


    def remove(self, key):
        ''' removes key, val pair from hash table '''
        idx = self._hash(key)
        self.table[idx] = [[k,v] for [k,v] in self.table[idx] if k is not key] 



    def get(self, key):
        ''' returns value with using key to look up in hash table '''
        idx = self._hash(key)

        # attempt to find item at table idx
        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                return self.table[idx][i][1]

        return "Key Does Not Exist."

    def __getitem__(self, key):
        ''' 
            usage:  hash_table[key]
                    will return the value at this key
        '''
        return self.get(key)

    def __setitem__(self, key, val):
        ''' 
            usage:  hash_table[key] = val
                    will set the value at this key or create new one
        '''
        self.insert(key, val)




if __name__ == "__main__":
    h = Hash_Table(11)
    h.show()
    h.insert(1, 'cat')
    h.show()
    h.insert('aa', 'dog')
    h.show()
    h.insert('z', 'giraffe')
    h.show()
    h.insert(33, 'donkey')
    h.show()
    h.insert(31, 'duh')
    h.show()
    h.insert(31, 'yep')
    h.show()

    print h.get(31)
    print h.get(32)

    h.remove(31)
    h.show()
    h.remove('aa')
    h.show()

    print h[1]
    h[1] = 'no more cat!'
    print h[1]


