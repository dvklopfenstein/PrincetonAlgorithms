"""A directed graph, implemented using an array of lists. Parallel edges & self-loops permitted."""
# pylint: disable=invalid-name
# ../algs4/src/main/java/edu/princeton/cs/algs4/Digraph.java

from AlgsSedgewickWayne.testcode.utils import adjtxtblk2OrderedDict

class Digraph:
    """A directed graph, implemented w/array of lists. Parallel edges & self-loops permitted."""

    def __init__(self, arr=None, **kwargs):
        if arr is not None:
            if isinstance(arr, int):
                ## print('DIGRAPH ARRAY INPUT:', arr)
                self._init_empty(arr)
            elif len(arr) == 1:
                self._init_empty(arr[0])
            else:
                self._init(arr)
            self.keys = range(self.num_vertices)
        elif 'adjtxt' in kwargs:
            self.adjs = adjtxtblk2OrderedDict(kwargs['adjtxt'])
            self.num_vertices = len(self.adjs)
            # pylint: disable=line-too-long
            self.num_edges = len(set(tuple(sorted([v, w])) for v, ws in self.adjs.items() for w in ws))
            self.keys = self.adjs.keys()

    def _init_empty(self, num_vertices):
        ## print(f'DIGRAPH INIT {num_vertices} VERTICES')
        if num_vertices < 0:
            raise RuntimeError("Number of vertices must be nonnegative")
        self.num_vertices = num_vertices # number of vertices
        self.num_edges = 0 # number of edges
        self.adjs = [set() for v in range(num_vertices)]
        self._indegree = [0]*num_vertices # indegree[v] = indegree of vertex v

    def _init(self, arr):
        """Initializes arr graph from an input stream."""
        # The format is the number of vertices V, followed by the number of edges E,
        # followed by E pairs of vertices, with each entry separated by whitespace.
        self._init_empty(arr[0]) # init V, and the empty adj list
        num_edges = arr[1]
        if num_edges < 0:
            raise RuntimeError("Number of edges must be nonnegative")
        for src_v, dst_w in arr[2:]:
            self.add_edge(src_v, dst_w)

    def add_edge(self, src_v, dst_w):
        """Adds the undirected edge src_v-dst_w to self graph."""
        #self._validateVertex(src_v)
        #self._validateVertex(dst_w)
        self.num_edges += 1
        self.adjs[src_v].add(dst_w)
        self._indegree[dst_w] += 1

    def adj(self, src_v):
        """Returns the vertices adjacent to vertex src_v."""
        #self._validateVertex(src_v)
        return self.adjs[src_v]

    def outdegree(self, src_v):
        """Returns the number of directed edges incident from vertex src_v."""
        #self._validateVertex(src_v)
        return len(self.adjs[src_v])

    def indegree(self, src_v):
        """Returns the number of directed edges incident to vertex src_v."""
        #self._validateVertex(src_v)
        return self._indegree[src_v]

    def reverse(self):
        """Get the reverse of the digraph."""
        rev_digraph = Digraph(self.num_vertices)
        for src_v in range(self.num_vertices):
            for dst_w in self.adjs(src_v):
                # pylint: disable=arguments-out-of-order
                rev_digraph.add_edge(dst_w, src_v)
        return rev_digraph

    #def _validateVertex(self, src_v):
    #    """raise an IndexOutOfBoundsException unless 0 <= src_v < V."""
    #    if src_v < 0 or src_v >= self.num_vertices or src_v not in self.adjs:
    #        raise Exception("vertex {} not between 0 and {} or in {}".format(
    #    src_v, self.num_vertices-1, self.adjs))

    def __str__(self):
        txt = [(f"{self.num_vertices} vertices, {self.num_edges} edges\n")]
        for src_v in self.keys:
            txt.append(f"{src_v}: ")
            for dst_w in self.adjs[src_v]:
                txt.append(f"{dst_w} ")
            txt.append("\n")
        return ''.join(txt)

    def __iter__(self): # Makes Graph an iterable.
        return iter(self.adjs) # returns an iterator.


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

#  Copyright 2002-present, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-present, DV Klopfenstein, PhD, Python implementation
