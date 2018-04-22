
# O(a) where a is the smaller of integers a, b
def recurs_multiply(a, b):
    ''' recursively multiplies two positive ints without using * operator '''

    # get smaller number to minimize time complexity
    smaller, bigger = (a, b) if a < b else (b, a)

    if smaller == 0: return 0
    if smaller == 1: return bigger

    return b + recurs_multiply(a-1, b)



# O(log(a)) where a is the smaller of integers a, b
def recurs_multiply2(a, b):
    ''' recursively multiplies two positive ints without using * operator '''

    # get smaller number to minimize time complexity
    smaller, bigger = (a, b) if a < b else (b, a)

    if smaller == 0: return 0
    if smaller == 1: return bigger

    # shift bits 1 to the right
    s = smaller >> 1
    half_prod = recurs_multiply2(s, bigger)

    # odd smaller number
    if smaller % 2 == 1:
        return half_prod + half_prod + bigger

    return half_prod + half_prod


if __name__ == "__main__":
    print recurs_multiply(3, 2) == 6
    print recurs_multiply(2, 3) == 6
    print recurs_multiply(20, 5) == 100
    print recurs_multiply(11, 3) == 33
    print recurs_multiply(2, 33) == 66

    print recurs_multiply2(3, 2) == 6
    print recurs_multiply2(2, 3) == 6
    print recurs_multiply2(20, 5) == 100
    print recurs_multiply2(11, 3) == 33
    print recurs_multiply2(2, 33) == 66
