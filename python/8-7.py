
def perm(s):
    ''' returns all permutations of string s '''
    n = len(s)
    if n == 0: return None
    if n == 1: return [s]

    c = s[0]
    perm_s = perm(s[1:])

    res = []

    # iterate through each string 
    for i in range(len(perm_s)):
        s1 = perm_s.pop(0)

        # iterate through each position in string
        for j in range(n):
            s2 = s1[:j] + c + s1[j:]
            res.append(s2)

    return res


def perm2(s):
    ''' returns all permutations of string s '''
    n = len(s)
    if n == 0: return None
    if n == 1: return [s]

    res = []

    for i in range(n):
        c = s[i]
        remaining = s[:i] + s[i+1:]
        perms = [c + p for p in perm2(remaining)]
        res.extend(perms)

    return res


if __name__ == "__main__":
    print perm('a')
    print perm('ab')
    print perm('abc')
    print perm('abcd')

    print perm2('a')
    print perm2('ab')
    print perm2('abc')
    print perm2('abcd')
