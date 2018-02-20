# Is Unique 
# O(N) where N = string length
import unittest

def is_unique(string):
    ''' returns True if a string has all unique characters '''
    if len(string) > 128: #assuming ASCII 0-127 chars
        return False

    chars = {}
    for char in string:
        if char in chars:
            return False
        else:
            chars[char] = True

    return True


class Test(unittest.TestCase):
    F = ("hello", "  ", "tttttt")
    T = ("yes", " ", ".!#$k4")

    def test_func(self):
        # False 
        for string in self.F:
            self.assertFalse(is_unique(string))
        # True 
        for string in self.T:
            self.assertTrue(is_unique(string))
        

if __name__ == "__main__":
    unittest.main()

