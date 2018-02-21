# One Away 
# O(N) where N = length of shorter string 
import unittest

def one_replace(str1, str2):
    ''' returns true if 2 equal length strings differ by 1 char '''
    found = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found:
                return False
            else:
                found = True
    return True


def one_insert(small, big):
    ''' returns true if small string only needs one insert to make strings equal '''
    for i in range(len(small)):
        if big[i] != small[i]:
            if big[i+1] != small[i]:
                return False
    return True


def one_away(str1, str2):   
    ''' returns true if strings are one char replace/remove/insert away from one another '''
    if len(str1) == len(str2):
        return one_replace(str1, str2)
    elif len(str1) + 1 == len(str2):  #str2 is bigger by 1
        return one_insert(str1, str2)
    elif len(str2) + 1 == len(str1):  #str1 is bigger by 1
        return one_insert(str2, str1)
    return False #more than 1 length difference between strings
        

class Test(unittest.TestCase):
    F = (
        ('pale', 'bake'),
        ('tacos', 'tac'),
        ('taco', 'poco')
        )
    T = (
        ('pale', 'ple'),
        ('pales', 'pale'), 
        ('pale', 'bale') 
        )

    def test_func(self):
        # False
        for strings in self.F:
            self.assertFalse(one_away(*strings))
        # True
        for strings in self.T:
            self.assertTrue(one_away(*strings))       

if __name__ == "__main__":
    unittest.main()

