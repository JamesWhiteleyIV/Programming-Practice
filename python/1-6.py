# String Compression 
# O(N) where N = length of string s
import unittest

def str_compress(s):
    ''' returns compressed string; s = aabbb  would return a2b3 '''
    if len(s) <= 2:
        return s

    res = []  #to store final string 
    c = s[0]
    count = 1 

    for i in range(1, len(s)):
        if s[i] == c:
            count += 1
        else:
            res.append(c)
            res.append(str(count))
            c = s[i]
            count = 1
        if i == len(s) - 1: #final char in string so append
            res.append(c)
            res.append(str(count))

    final = ''.join(res)
    if len(final) < len(s):
        return final 
    return s


class Test(unittest.TestCase):
    data = (
        ('',''),
        ('a','a'),
        ('aa','aa'),
        ('aab','aab'), #a2b1 longer
        ('aabb','aabb'), #a2b2 same size
        ('aabbb','a2b3'),
        ('aaabbb','a3b3'),
        ('aaabbbhhhhh','a3b3h5'),
        )

    def test_func(self):
        for actual, expected in self.data:
            self.assertEqual(str_compress(actual), expected)

if __name__ == "__main__":
    unittest.main()
