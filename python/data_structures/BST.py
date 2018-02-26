# Binary Search Tree Implementation 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.data)

    
    def insert(self, data):
        if self.data is None:
            self.data = data 
        else:
            if data <= self.data: # go left
                if self.left is None:   
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else: # go right
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                
 
    def _find_node_and_parent(self, data):
        ''' returns parent of node with data and the node
            node will == None if the data DNE 
            parent will == None if the data is the root node 
        '''
        parent = None
        node = self

        # loop until we find the node
        while node is not None: 
            if node.data == data:
                return parent, node

            parent = node
            if data <= node.data:
                node = node.left
            else:
                node = node.right

        return parent, node
 

    def _find_min(self, node):
        ''' returns data with smallest value of all child nodes '''
        cur = node 
        while cur.left:
            cur = cur.left
        return cur.data


    def remove(self, data):
        ''' removes first node that matches the data '''
        parent, node = self._find_node_and_parent(data)
        
        if node is None: #data DNE
            return False

        if node.left is None and node.right is None: #no children
            if parent is None: #only root node in tree cannot remove it
                return False
            elif parent.left is node: 
                parent.left = None
            else: 
                parent.right = None

        elif node.left and node.right: #both children
            # locate and remove the smallest value in right subtree
            min_val = self._find_min(node.right)
            self.remove(min_val)
            # set node's data to be smallest value that was found
            node.data = min_val

        elif node.right:  #only a right child
            if parent is None: #change root to right child
                node.data = node.right.data
                node.left = node.right.left
                node.right = node.right.right
            elif parent.left is node:
                parent.left = node.right
            else:
                parent.right = node.right
                
        else: #only a left child
            if parent is None: #change root to right child
                node.data = node.left.data
                node.right = node.left.right
                node.left = node.left.left
            elif parent.left is node:
                parent.left = node.left
            else:
                parent.right = node.left
                

    def print_in_order(self):   
        if self.left:
            self.left.print_in_order()
        print self.data
        if self.right:
            self.right.print_in_order()
 

    def print_pre_order(self):   
        print self.data
        if self.left:
            self.left.print_pre_order()
        if self.right:
            self.right.print_pre_order()


    def print_post_order(self):   
        if self.left:
            self.left.print_post_order()
        if self.right:
            self.right.print_post_order()
        print self.data


    def build(self, *data):
        ''' pass in variable amount of data and add to tree in order '''
        for val in data:
            self.insert(val)

            

    
           
if __name__ == "__main__":
    print "Testing BST"
    root = Node(5) 
    root.build(2, 12, -4, 3, 9, 21, 19, 25, -5)
    root.print_in_order()
    print '----------------------------'
    print 'remove 18 DNE'
    root.remove(18)
    root.print_in_order()
    print '----------------------------'
    print 'remove -4 (only left child)'
    root.remove(-4)
    root.print_in_order()
    print '----------------------------'
    print 'remove -5 (no children)'
    root.remove(-5)
    root.print_in_order()
    print '----------------------------'
    print 'remove 2 (only right child)'
    root.remove(2)
    root.print_in_order()
    print '----------------------------'
    print 'remove 5 (2 children)'
    root.remove(5)
    root.print_in_order()
    print '----------------------------'
    print 'add 5'
    root.insert(5)
    root.print_in_order()
    print '----------------------------'
    print 'add 5'
    root.insert(5)
    root.print_in_order()
    print '----------------------------'
    print 'add 7'
    root.insert(7)
    root.print_in_order()
    print '----------------------------'
    print "remove 5"
    root.remove(5)
    root.print_in_order()
    print '----------------------------'
    print "remove 5"
    root.remove(5)
    root.print_in_order()
    print '----------------------------'
    print "remove 9"
    root.remove(9)
    root.print_in_order()
    print '----------------------------'

