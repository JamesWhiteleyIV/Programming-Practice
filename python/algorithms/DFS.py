import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Node:
    def __init__(self, value=None):
        self.value = value
        self.visited = False
        self.neighbors = []


'''
generates a simple graph

root -> A -> B -> E
          -> C -> goal 
'''
def graph_gen():
    root = Node('root')
    A = Node('A') 
    B = Node('B') 
    C = Node('C') 
    E = Node('E') 
    goal = Node('goal') 

    B.neighbors = [E]
    C.neighbors = [goal]
    A.neighbors = [B, C]
    root.neighbors = [A]

    return root
    


#iterates through neighbors and returns first unvisited node it finds
def find_unvisited(node):
    for n in node.neighbors:
        if not n.visited:
            return n

    return None


def dfs(root, val):
    s = [] #init stack 

    root.visited = True
    print "order of node visiting:"

    print root.value
    s.append(root)

    # root is goal node
    if root.value == val:
        return

    #while stack is not empty
    while s != []:
        child = find_unvisited(s[-1])
        if child is None: #reached end, no neighbors
            s.pop(-1)
        else:
            child.visited = True
            s.append(child)
            print child.value
            if child.value == val:
                return
            
        
       

if __name__ == "__main__":
    root = graph_gen()
    print "DFS:"
    dfs(root, 'goal')

