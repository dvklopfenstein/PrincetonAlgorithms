"""A undirected graph, implemented using an array of sets. Parallel edges and self-loops allowed."""

import sys
from AlgsSedgewickWayne.testcode.utils import adjtxtblk2OrderedDict

class Graph:
    """Undirected graph"""

    def __init__(self, arg=None, **kwargs):
        if arg is not None:
            if isinstance(arg, int):
                self._init_empty(arg)
            elif len(arg) == 1:
                self._init_empty(arg[0])
            else:
                self._init(arg)
            self.keys = range(self.num_nodes)
        elif 'adjtxt' in kwargs:
            self._adj = adjtxtblk2OrderedDict(kwargs['adjtxt'])
            self.num_nodes = len(self._adj)
            self.num_edges = self._init_num_edges()
            self.keys = self._adj.keys()

    def V(self):
        """Returns the number of vertices in self graph."""
        return self.num_nodes

    def E(self):
        """Returns the number of edges in self graph."""
        return self.num_edges

    def addEdge(self, node_v, node_w):
        """Adds the undirected edge node_v-node_w to self graph."""
        self.add_edge(node_v, node_w)

    def add_edge(self, node_v, node_w):
        """Adds the undirected edge node_v-node_w to self graph."""
        #self._validateVertex(node_v)
        #self._validateVertex(node_w)
        self.num_edges += 1
        self._adj[node_v].add(node_w)
        self._adj[node_w].add(node_v)

    def adj(self, node_v):
        """Returns the vertices adjacent to vertex node_v."""
        #self._validateVertex(node_v)
        return self._adj[node_v]

    def degree(self, node_v):
        """Returns the degree of vertex node_v."""
        #self._validateVertex(node_v)
        return self._adj[node_v].size()

    #def _validateVertex(self, node_v):
    #  """raise an IndexOutOfBoundsException unless 0 <= node_v < V."""
    #  if node_v < 0 or node_v >= self.num_nodes or node_v not in self._adj:
    #    raise Exception("vertex {} is not between 0 and {} or in {}".format(
    #        node_v, self.num_nodes-1, self._adj))

    def __str__(self):
        txt = [(("{V} vertices, {E} edges\n").format(V=self.num_nodes, E=self.num_edges))]
        for node_v in self.keys:
            txt.append("{node_v}: ".format(node_v=node_v))
            for node_w in self._adj[node_v]:
                txt.append("{node_w} ".format(node_w=node_w))
            txt.append("\n")
        return ''.join(txt)

    def __iter__(self): # Makes Graph an iterable.
        return iter(self._adj) # returns an iterator.

    def wr_png(self, fout_png="Graph.png", prt=sys.stdout, **kwargs):
        """Make a png showing a diagram of the connected components."""
        import pydot
        # 1. create/initialize graph
        graph = pydot.Dot(graph_type='graph') # undirected graph
        # 2. create nodes
        nodes = [pydot.Node(node_v) for node_v in self.keys]
        # 3. add nodes to graph
        for node in nodes:
            graph.add_node(node)
        # 4. add edges between nodes to graph
        for node_v, node_w in self.get_edges():
            if node_v != node_w: # print only edges from one node to another (not to self)
                graph.add_edge(pydot.Edge(node_v, node_w))
        # 5. write graph to png file
        graph.write_png(fout_png)
        prt.write("  wrote: {}\n".format(fout_png))

    def get_edges(self):
        """Get edges"""
        edges = set()
        for node_v in self.keys:
            for node_w in self._adj[node_v]:
                edges.add(tuple(sorted([node_v, node_w])))
        return edges

    def _init_empty(self, num_nodes):
        """Initialize an empty graph containing N nodes"""
        if num_nodes < 0:
            raise Exception("Number of vertices must be nonnegative")
        self.num_nodes = num_nodes
        self.num_edges = 0
        self._adj = [set() for node_v in range(num_nodes)]

    def _init(self, arg):
        """Initializes arg graph from an input stream."""
        # The format is the number of vertices V, followed by the number of edges E,
        # followed by E pairs of vertices, with each entry separated by whitespace.
        self._init_empty(arg[0]) # init V, and the empty adj list
        edge = arg[1]
        if edge < 0:
            raise Exception("Number of edges must be nonnegative")
        for node_v, node_w in arg[2:]:
            self.add_edge(node_v, node_w)

    def _init_num_edges(self):
        """Get the number of edges"""
        edges = set()
        for node_v, nodes in self._adj.items():
            for node_w in nodes:
                edges.add(frozenset([node_v, node_w]))
        return len(edges)

 #*****************************************************************************/
 #  % Graph.py ../thirdparty/tinyG.txt
 #  13 vertices, 13 edges
 #  0: 6 2 1 5
 #  1: 0
 #  2: 0
 #  3: 5 4
 #  4: 5 6 3
 #  5: 3 4 0
 #  6: 0 4
 #  7: 8
 #  8: 7
 #  9: 11 10 12
 #  10: 9
 #  11: 9 12
 #  12: 11 9
 #
 #*****************************************************************************/

# -----------------------------------------------------------------------------
# INTRODUCTION TO GRAPHS (9:32)


# SOME GRAPH-PROCESSING PROBLEMS 08:14
#
# PATH: Is there a path between s and t?
# SHORTEST PATH: What is the shortest path between s and t?
#
# CYCLE: Is there a cycle in the graph?
# EULER TOUR: Is there a cycle that uses each edge exactly once?
# HAMILTON TOUR: Is there a cycle that uses each vertex exactly once?
#
# CONNECTIVITY: Is there a awy to connect all of the vertices?
# MST: What is the best way to connect all of the vertices?
# BICONNECTIVITY: Is there a vertex whose removeal disconnects the graph?
#
# PLANARITY: Can you draw the graph in the plane with no crossing edges?
# GRAPH ISOMORPHISM: Do two adjacency lists represent the same graph?
#
# CHALLENGE: Whinc of these problems are easy? difficult? intractable?



# QUESTION: A cycle that uses eachedge of a graph exactly once is called
# ANSWER: An Euler tour

#  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2019, DV Klopfenstein, Python implementation
