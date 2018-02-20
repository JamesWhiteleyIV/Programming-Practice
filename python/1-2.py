# Check Permutation 
# O(2N) = O(N) where N = length of string 
import unittest

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = {}
    for i in range(len(str1)):
        char = str1[i]
        if char in chars: #check if character exists
            chars[char] += 1 
        else:
            chars[char] = 1

    for i in range(len(str2)):
        char = str2[i]
        if char in chars:
            if chars[char] == 0:
                return False
            else:
                chars[char] -= 1
        else:
            return False

    return True
                
            
class Test(unittest.TestCase):
    # False data
    F = (
        ('jfjfj', 'jfjfA'),
        ('0001', '1100'),
        ('wifi', 'fipi')
    )

    # True data
    T = (
        ('1100', '0011'),
        ('kayak', 'kayak'),
        ('wifi', 'fiwi')
    )

    def test_func(self):
        # False 
        for strings in self.F:
            self.assertFalse(check_permutation(*strings))
        # True 
        for strings in self.T:
            self.assertTrue(check_permutation(*strings))
        

if __name__ == "__main__":
    unittest.main()
