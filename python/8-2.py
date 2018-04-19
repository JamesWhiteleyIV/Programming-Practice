# Robot in a grid

# non - recursive BFS approach
def find_path(grid):
    '''
        finds a path using modified BFS for a robot that can only go down or right
        in a grid.  Using -1 to represent blockage. 
    '''
    rows = len(grid)
    cols = len(grid[0])
    goal = (rows-1, cols-1)

    visited = []
    r = 0
    c = 0
    q = [(r,c)]

    while q != []:
        cur = q.pop(0)
        visited.append(cur)

        # found last cell, return route of visited cells
        if cur == goal:
            return visited

        r = cur[0]
        c = cur[1]

        # make sure path to right does not go
        # out of grid bounds or have a blockage
        if r + 1 < rows:
            if grid[r+1][c] != -1:
                #print 'new row+1', (r+1, c)
                q.append( (r+1, c) )

        if c + 1 < cols:
            if grid[r][c+1] != -1:
                #print 'new col+1', (r, c+1)
                q.append( (r, c+1) )           

    return "No Path Exists"





if __name__ == "__main__":
    print "---------------TESTING PATH EXISTS-----------------"
    grid = [
        [0,  0,  0,  0],
        [0, -1, -1,  0],
        [0,  0,  0, -1],
        [-1, 0, -1,  0], [0,  0,  0,  0],
    ]

    print find_path(grid)


    print "---------------TESTING PATH DOES NOT EXIST-----------------"
    grid = [
        [0,  0,  0,  0],
        [0, -1, -1,  0],
        [0,  0,  0, -1],
        [-1, -1, -1,  -1],
        [0,  0,  0,  0],
    ]

    print find_path(grid)
