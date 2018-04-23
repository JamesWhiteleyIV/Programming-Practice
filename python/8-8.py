
def perm_helper(s):
    ''' removes all duplicate chars '''
    d = {}
    new_s = "" 

    for i in range(len(s)):
        c = s[i]
        if c not in d:
            d[c] = True
            new_s += c

    return perm_with_dups(new_s)
            
    

def perm_with_dups(s):
    ''' returns all permutations of string s '''
    n = len(s)
    if n == 0: return None
    if n == 1: return [s]

    res = []

    for i in range(n):
        c = s[i]
        remaining = s[:i] + s[i+1:]
        perms = [c + p for p in perm_with_dups(remaining)]
        res.extend(perms)

    return res


if __name__ == "__main__":
    print perm_helper('a')
    print perm_helper('ab')
    print perm_helper('abc')
    print perm_helper('aabc')
