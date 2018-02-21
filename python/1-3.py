# URLify 
# O(N) where N = string length  
import unittest

def easyURLify(string):
    ''' replaces all spaces with %20 using standard Python function '''
    return string.replace(" ", "%20")
    
def URLify(string):
    ''' replaces all spaces with %20 '''
    final_str = []
    space = ' '
    for c in string:
        if c == space:
            final_str.append("%20")
        else:
            final_str.append(c)
    return ''.join(final_str)

            
class Test(unittest.TestCase):
    str1 = "test me"
    str2 = "testme"
    str3 = " a b c d "

    def test_easy(self):
        self.assertEqual(easyURLify(self.str1), "test%20me")
        self.assertEqual(easyURLify(self.str2), "testme")
        self.assertEqual(easyURLify(self.str3), "%20a%20b%20c%20d%20")
 
    def test_func(self):
        self.assertEqual(URLify(self.str1), "test%20me")
        self.assertEqual(URLify(self.str2), "testme")
        self.assertEqual(URLify(self.str3), "%20a%20b%20c%20d%20")           

if __name__ == "__main__":
    unittest.main()

