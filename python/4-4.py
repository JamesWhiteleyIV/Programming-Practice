# Check Balanced 
from data_structures.BST import Node 


def height(node, h):
    ''' returns max height of a node '''
    if node is None:
        return h  # previous height is max height

    h += 1
    return max(height(node.left, h), height(node.right, h))
   

def is_balanced(root):
    ''' returns True if binary tree is balanced (heights of 2 subtrees never off by more than 1) ''' 
    if root is None:
        return True

    else:
        diff = height(root.left, 1) - height(root.right, 1)
        if diff > 1:
            return False
        else:
            return is_balanced(root.left) and is_balanced(root.right)



if __name__ == "__main__":
    print '-----------------------'
    root = Node(4)
    root.build(2, 12, -4, 3, 9, 21, 19, 25, -5)
    print 'testing is_balanced on balanced tree:'
    print "is_balanced() == ", is_balanced(root)

    print '-----------------------'
    root = Node(4)
    root.build(2, 12, -4, 3, 9, 21, 19, 25, -5, -6)
    print 'testing is_balanced on Unbalanced tree:'
    print "is_balanced() == ", is_balanced(root)

    print '-----------------------'
    root = Node(4)
    print 'testing is_balanced on tree with 1 node:'
    print "is_balanced() == ", is_balanced(root)


