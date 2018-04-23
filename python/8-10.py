# Paint fill

def paint_fill(m, p, new_color, cur_color=None):
    '''
        given a 2d matrix m, and a point p in tuple format (x, y), 
        and a new_color in string format 'b',
        fills in surrounding area until color changes.
    '''
    r, c = p

    # check bounds of point
    if r >= len(m) or r < 0 or c >= len(m[0]) or c < 0:
        return False

    if cur_color == None:
        cur_color = m[r][c]

    # hit new color border
    if m[r][c] != cur_color:
        return False

    # fill current point with new color
    m[r][c] = new_color

    #try filling up, left, down, right 
    paint_fill(m, (r,c+1), new_color, cur_color)
    paint_fill(m, (r,c-1), new_color, cur_color)
    paint_fill(m, (r+1,c), new_color, cur_color)
    paint_fill(m, (r-1,c), new_color, cur_color)

    return True


if __name__ == "__main__":
    m = [
        ['w', 'w', 'w', 'w', 'w', 'w'],
        ['b', 'b', 'b', 'w', 'w', 'w'],
        ['w', 'w', 'b', 'w', 'w', 'w'],
        ['w', 'w', 'b', 'w', 'w', 'w'],
    ]

    for row in m:
        print row 

    p = (3, 1)
    paint_fill(m, p, 'g')
    print '-----------------------------------'

    for row in m:
        print row        

    print '-----------------------------------'
    p = (0, 0)
    paint_fill(m, p, 'p')

    for row in m:
        print row      
