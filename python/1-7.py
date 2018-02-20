# Rotate Matrix 
# O(N^2) where N = length of N x N matrix
import unittest

def init_matrix(n):
    ''' returns a matrix filled with 0's of size n x n '''
    return [[0 for i in range(n)] for j in range(n)]


def rot_matrix(m):
    ''' rotates a matrix 90 degrees clockwise '''
    rot_m = init_matrix(len(m)) 
    n = len(m) - 1
    cur = 0
    for i in range(len(m)):
        for j in range(len(m)):
            rot_m[cur][n] = m[i][j]
            cur += 1
        cur = 0
        n -= 1
    return rot_m


def alt_rot_matrix(m):
    ''' rotates a matrix 90 degrees clockwise in place '''
    n = len(m)
    if n == 0: return False
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i] #save top

            # left -> top
            m[first][i] = m[last-offset][first]

            # bottom -> left
            m[last-offset][first] = m[last][last-offset]
        
            # right -> bottom 
            m[last][last-offset] = m[i][last]
 
            # top -> right 
            m[i][last] = top 

    return m
        

class Test(unittest.TestCase):

    m2 = [
        [1, 2],
        [3, 4]
    ]

    exp_m2 = [
        [3, 1],
        [4, 2]
    ]
    
    m4 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]

    exp_m4 = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4],
    ]

    def test_func(self):
        self.assertEqual(rot_matrix(self.m2), self.exp_m2)
        self.assertEqual(rot_matrix(self.m4), self.exp_m4)

    def test_func_alt(self):
        self.assertEqual(alt_rot_matrix(self.m2), self.exp_m2)
        self.assertEqual(alt_rot_matrix(self.m4), self.exp_m4)


if __name__ == "__main__":
    unittest.main()
