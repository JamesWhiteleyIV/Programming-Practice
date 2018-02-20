# String Rotation 
# O(N) where N = length of string
import unittest

def is_rotation(s1, s2):
    ''' given two strings, checks if s2 is a rotation of s1 using only one call to isSubstring '''
    if len(s1) != len(s2):
        return False # must be same length
    return s2 in s1 + s1 


class Test(unittest.TestCase):
    data = [
        ("aabb", "abba", True),
        ("watermelon", "atermelonw", True),
        ("watermelon", "nwatermelo", True),
        ("atermwelon", "atermelonw", False),
        ("aaabb", "aaab", False),
        ("abb", "abbb", False),
    ]

    def test_func(self):
        for [s1, s2, expected] in self.data:
            self.assertEqual(is_rotation(s1, s2), expected)

    
if __name__ == "__main__":
    unittest.main()

