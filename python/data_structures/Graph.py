# Directed and Unidrected Graph implementations
# Breadth-first and Depth-first search implementations

class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = {}

    def add_neighbor(self, node, weight=1): 
        self.adjacent[node] = weight


class Graph:
    def __init__(self, directed=True):
        self.nodes = {} 
        self._directed = directed

    def __str__(self):
        data = '' 
        for node in self.nodes:
            data += str(self.nodes[node].data) + ': '
            adj = [str(x) for x in self.nodes[node].adjacent]
            adj = ', '.join(adj)
            data += adj 
            data += '\n'
        return data

    def __len__(self):
        return len(self.nodes)

    def add_node(self, data):
        if data not in self.nodes:
            self.nodes[data] = Node(data)

    def add_edge(self, node1, node2, weight=1):
        ''' add edge from node1->node2
            if undirected, also add connection from node2->node1
            adds the node data if not in graph 
            updates edge weight if edge exists already
        '''
        if node1 not in self.nodes:
            self.nodes[node1] = Node(node1)
        if node2 not in self.nodes:
            self.nodes[node2] = Node(node2)
        
        #add edge from node1 -> node2
        self.nodes[node1].add_neighbor(node2, weight)

        #add edge from node2 -> node1 if undirected graph 
        if not self._directed: 
            self.nodes[node2].add_neighbor(node1, weight)

    def remove_node(self, node):
        ''' remove node and all incident edges '''
        n = node
        for node in self.nodes:
            if n in self.nodes[node].adjacent:
                del self.nodes[node].adjacent[n]
        del self.nodes[n]


    def build(self, connections):
        ''' pass in list of tuples [('A', 'B'), ('B', 'C')] or [('A', 'B', 2), ('B', 'C', 4)] for weighted
            and will create connections from A->B and B->C
            if undirected it will create A->B, B->A, B->C and C->B
        '''
        # if unweighted graph
        if len(connections[0]) == 2:
            for node1, node2 in connections:
               self.add_edge(node1, node2)

        # weighted graph
        else:
            for node1, node2, weight in connections:
               self.add_edge(node1, node2, weight)


    def weights(self):
        for node in self.nodes:
            for adj in self.nodes[node].adjacent:
                weight = self.nodes[node].adjacent[adj]
                print '(' + str(node) + ', ' +  str(adj) + ',',  str(weight) + ')'


       

class Simple_Graph:
    ''' unweighted, directed or undirected graph '''
    def __init__(self, directed=True):
        self.data = {}
        self.directed = directed


    def add_node(self, node):
        if node not in self.data:
            self.data[node] = [] 
    
    def add_edge(self, node1, node2):
        ''' add edge from node1->node2 '''
        if node1 in self.data and node2 in self.data: # both nodes must exist

            if node2 not in self.data[node1]: #not already an edge
                self.data[node1].append(node2)

                if not self.directed:
                    self.add_edge(node2, node1)


    def remove_node(self, node):
        if node in self.data: #node exists
            for key in self.data: 
                if node in self.data[key]: #if a node is connected to del node
                    self.data[key].remove(node) #del it
            del self.data[node]


    def remove_edge(self, node1, node2):
        ''' remove edge from node1->node2 '''
        if node1 in self.data and node2 in self.data: # both nodes must exist

            if node2 in self.data[node1]: 
                self.data[node1].remove(node2) #del it

                if not self.directed: #undirected graph remove edge from node2->node1 also
                    self.remove_edge(node2, node1)


    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)
            

    def add_edges(self, edges):
        for node1, node2 in edges:
            self.add_edge(node1, node2)

    def generate(self):
        nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        edges = (
            ('A', 'G'),
            ('A', 'C'),
            ('B', 'C'),
            ('E', 'G'),
            ('E', 'F'),
            ('F', 'G'),
            ('D', 'A'),
            ('D', 'C'),
            ('G', 'D'),
            )
        self.add_nodes(nodes)
        self.add_edges(edges)


                   
if __name__ == "__main__":
    g = Simple_Graph(False)
    g.generate()
    print g.data
    print "Removing node A..."
    g.remove_node('A')
    print g.data
    print "Removing edge F -> E..."
    g.remove_edge('F', 'E')
    print g.data














