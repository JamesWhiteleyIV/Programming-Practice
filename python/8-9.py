
# O(n) 
def parens(n):
    if n == 1: return set(['()'])

    # get list of n-1 answers
    prev = parens(n-1)

    res = set([])
    for i in prev:
        res.add('()' + i) 
        res.add('(' + i + ')')
        res.add(i + '()')

    return res 

# didn't need to use memoization, DOH!
def parens_memo(n, memo={}):
    if n == 1: return set(['()'])
    if n in memo: return memo[n]

    # get list of n-1 answers
    # this will be O(1) if already in memo
    prev = parens(n-1, memo)

    memo[n] = set([])
    for i in prev:
        memo[n].add('()' + i) 
        memo[n].add('(' + i + ')')
        memo[n].add(i + '()')

    return memo[n]


if __name__ == "__main__":
    print parens(1)
    print parens(2)
    print parens(3)
    print parens(4)
