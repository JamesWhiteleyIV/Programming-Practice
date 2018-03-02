# Build Order 
from data_structures.BST import Node 

def remove_dep(g, order=[]):
    for key in g:
        if g[key] == []:
            if key in order:
                return g, False
            order.append(key)
            for k in g:   # remove built dependency from project
                if key in g[k]:
                    g[k].remove(key)
            del g[key]
            return remove_dep(g, order)
    return g, order


def find_build_order(projects, dependencies):
    ''' returns order of build or error if no valid build order '''

    # build graph
    g = {}
    for p in projects:
        g[p] = []

    # add dependencies
    for p, d in dependencies:
        g[d].append(p)

    # if a project has no dependencies, build it and
    # remove it from all other projects
    g, order = remove_dep(g)

    return order

        
        



if __name__ == "__main__":
    print '---------------------------------------'
    print "True test"
    projects = ('a', 'b', 'c', 'd', 'e', 'f')
    dependencies = (
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c'),
        )

    print find_build_order(projects, dependencies)


    print '---------------------------------------'
    print "False test"
    projects = ('a', 'b', 'c', 'd', 'e', 'f')
    dependencies = (
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c'),
        ('d', 'a'),
        )

    print find_build_order(projects, dependencies)


    print '---------------------------------------'
    print "False test"
    projects = ('a', 'b', 'c', 'd', 'e', 'f')
    dependencies = (
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c'),
        ('e', 'c'),
        )

    print find_build_order(projects, dependencies)


