# Zero Matrix 
# O(MxN) where M = row length and N = column length of MxN matrix 
# iterates MxN 2x which is still O(MxN)
import unittest

def zero_matrix(m):
    ''' if an element in an M x N matrix is 0 its entire row and column are set to 0 '''
    r = {}
    c = {}
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 0:
                r[row] = True
                c[col] = True

    for row in range(len(m)):
        for col in range(len(m[row])):
            if row in r or col in c:
                m[row][col] = 0

    return m


class Test(unittest.TestCase):
    # 2x3 matrix
    m2_3 = [ 
        [1, 0, 3],
        [2, 5, 6],
    ]
    exp_m2_3 = [ 
        [0, 0, 0],
        [2, 0, 6],
    ]

    # 2x2 matrix
    m2 = [
        [0, 2],
        [3, 4]
    ]
    exp_m2 = [
        [0, 0],
        [0, 4]
    ]
    
    # 4x4 matrix
    m4 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  0,  11, 12],
        [13, 14, 15, 16],
    ]
    exp_m4 = [
        [1,  0,  3,  4],
        [5,  0,  7,  8],
        [0,  0,  0,  0],
        [13, 0, 15, 16],
    ]

    def test_func(self):
        self.assertEqual(zero_matrix(self.m2_3), self.exp_m2_3)
        self.assertEqual(zero_matrix(self.m2), self.exp_m2)
        self.assertEqual(zero_matrix(self.m4), self.exp_m4)

    
if __name__ == "__main__":
    unittest.main()
