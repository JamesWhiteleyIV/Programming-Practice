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


def bfs(root, val):
    q = [] #init queue
    root.visited = True
    print "order of node visiting:"

    print root.value
    q.append(root)

    # root is goal node
    if root.value == val:
        return

    while q != []:
        n = q.pop()
        child = find_unvisited(n)

        while child is not None:
            child.visited = True
            q.append(child)
            print child.value
            child = find_unvisited(n)

    
 
           
        
       

if __name__ == "__main__":
    root = graph_gen()
    print "BFS:"
    bfs(root, 'goal')


