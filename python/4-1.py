# Route Between Nodes 
from data_structures.Graph import Simple_Graph 


def route(graph, node1, node2, visited={}):
    ''' returns True if route between nodes of directed graph '''
    found = False
    for node in graph.data[node1]:
        if node in visited:
            return False
        if node == node2:
            return True
        else:   
            visited[node] = True
            found = route(graph, node, node2, visited)
            if found:
                return True
    return False
    

if __name__ == "__main__":
    g = Simple_Graph() 
    g.generate()

    print g.data
    
    print route(g, 'A', 'D') # True
    print route(g, 'A', 'B') # False
    print route(g, 'G', 'C') # True
    print route(g, 'B', 'C') # True
    print route(g, 'D', 'F') # False 
    
