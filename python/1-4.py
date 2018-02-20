# Palindrome Permutation 
# O(N) where N = length of string
# clarify spaces, upper case, lower case
import unittest

def palperm(string):
    ''' returns true if string is a permutation of a palindrome'''
    d = {}
    for c in string:
        c = c.lower()
        if c != ' ':
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

    one_odd = False
    for key in d:
        if d[key] % 2 != 0: #odd num  
            if not one_odd:
                one_odd = True
            else:
                return False
    return True
    

class Test(unittest.TestCase):
    str1 = "Tact Coa" # True
    str2 = "tac coa"  # False
    str3 = "a a b b " # True
    str4 = "kayak"    # True

    def test_func(self):
        self.assertTrue(palperm(self.str1))
        self.assertFalse(palperm(self.str2))
        self.assertTrue(palperm(self.str3))           
        self.assertTrue(palperm(self.str4))           

if __name__ == "__main__":
    unittest.main()
