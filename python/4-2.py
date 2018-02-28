# Minimal Tree
from data_structures.BST import Node 


def ins_right(root, array, pos):
    left = pos + 2 
    mid = pos + 3
    right = pos + 4 

    if mid < len(array):
        root.insert(array[mid])
    if left < len(array):
        root.insert(array[left])
    if right < len(array):
        root.insert(array[right])
        root = ins_right(root, array, mid)
    
    return root


def ins_left(root, array, pos):
    left = pos - 4 
    mid = pos - 3
    right = pos - 2 

    if mid >= 0:
        root.insert(array[mid])
    if right >= 0:
        root.insert(array[right])
    if left >= 0:
        root.insert(array[left])
        root = ins_left(root, array, mid)
    
    return root


def min_tree(array):
    ''' 
        given an increasing order sorted array with unique integers,
        returns binary search tree with minimal height
    '''
    mid = len(array) / 2 # middle position for odd array, middle - 1 for even
    root = Node(array[mid])
    if len(array) >= 3:
        root.insert(array[mid-1])
        root.insert(array[mid+1])
    root = ins_right(root, array, mid)
    root = ins_left(root, array, mid)

    return root


if __name__ == "__main__":
    array = [1, 3, 4, 11, 12, 21, 41, 44, 45]
    tree = min_tree(array)
    tree.print_pre_order()
    print '-----------------------------'
    tree.print_post_order()
    print '-----------------------------'
    tree.print_in_order()

   
