# Validate BST 
from data_structures.BST import Node 


def check_order(node, minimum, maximum):
    ''' recursively checks a node and all its children for correct bst order '''
    if node is None:
        return True

    if ((minimum != None and node.data <= minimum) or (maximum != None and node.data > maximum)):
        return False

    if (not check_order(node.left, minimum, node.data) or not check_order(node.right, node.data, maximum)):
        return False

    return True


def is_bst(root):
    ''' returns True is tree is a binary search tree '''
    return check_order(root, None, None)


if __name__ == "__main__":
    print '-----------------------'
    root = Node(4)
    root.build(2, 12, -4, 3, 9, 21, 19, 25, -5)
    print 'testing is_bst on binary search tree:'
    print "is_bst() == ", is_bst(root)

    print '-----------------------'
    print 'changing root node to 10000 to no longer be balanced'
    root.data = 10000
    print 'testing is_bst on binary search tree:'
    print "is_bst() == ", is_bst(root)

