# Minimal Tree
from data_structures.BST import Node 


def min_tree(array):
    return ins(array, 0, len(array) - 1)


def ins(array, start, end):
    if end < start:
        return None

    mid = (start + end) / 2
    root = Node(array[mid])
    root.left = ins(array, start, mid - 1)
    root.right = ins(array, mid + 1, end)
    return root
    

if __name__ == "__main__":
    print "array:"
    array = [1, 3, 4, 11, 12, 21, 41, 44, 45]
    print array
    tree = min_tree(array)
    print "Pre-order:"
    tree.print_pre_order()
    print '-----------------------------'
    print "Post-order:"
    tree.print_post_order()
    print '-----------------------------'
    print "In-order:"
    tree.print_in_order()

   
