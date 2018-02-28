import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_structures.Graph import Graph 
from data_structures.Queue import Queue 

def bfs(graph, val):
    #init queue
    visited = {} 
    q = Queue()
    q.add(start)

    while not q.is_empty():
        cur = q.remove()
        adj = graph.nodes[cur]
        for 
        print cur
        
        
    






if __name__ == "__main__":
    #init directed graph
    g = Graph()
    data = [
        ('A', 'B'),
        ('D', 'C'),
        ('A', 'C'),
        ('B', 'A'),
        ]
    g.build(data)

    bfs(g, 'A')


