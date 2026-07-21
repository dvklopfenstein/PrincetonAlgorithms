"""run DFS in digraph dag from vertex v and compute preorder/postorder"""
# Described in the lecture, "Topological Sort," in "Lecture 13: Directed Graphs"
#
# /******************************************************************************
#  *  Compilation:  javac DepthFirstOrder.java
#  *  Execution:    java DepthFirstOrder digraph.txt
#  *  Dependencies: Digraph.java Queue.java Stack.java StdOut.java
#  *                EdgeWeightedDigraph.java DirectedEdge.java
#  *  Data files:   https://algs4.cs.princeton.edu/42digraph/tinyDAG.txt
#  *                https://algs4.cs.princeton.edu/42digraph/tinyDG.txt
#  *
#  *  Compute preorder and postorder for a digraph or edge-weighted digraph.
#  *  Runs in O(E + V) time.
#  *
#  *  % java DepthFirstOrder tinyDAG.txt
#  *     v  pre post
#  *  --------------
#  *     0    0    8
#  *     1    3    2
#  *     2    9   10
#  *     3   10    9
#  *     4    2    0
#  *     5    1    1
#  *     6    4    7
#  *     7   11   11
#  *     8   12   12
#  *     9    5    6
#  *    10    8    5
#  *    11    6    4
#  *    12    7    3
#  *  Preorder:  0 5 4 1 6 9 11 12 10 2 3 7 8
#  *  Postorder: 4 5 1 12 11 10 9 6 0 3 2 7 8
#  *  Reverse postorder: 8 7 2 3 0 6 9 10 11 12 1 5 4
#  *
#  ******************************************************************************/
#
# package edu.princeton.cs.algs4
#
# /**
#  *  The {@code DepthFirstOrder} class represents a data type for
#  *  determining depth-first search ordering of the vertices in a digraph
#  *  or edge-weighted digraph, including preorder, postorder, and reverse postorder.
#  *  <p>
#  *  This implementation uses depth-first search.
#  *  Each constructor takes &Theta;(<em>V</em> + <em>E</em>) time,
#  *  where <em>V</em> is the number of vertices and <em>E</em> is the
#  *  number of edges.
#  *  Each instance method takes &Theta;(1) time.
#  *  It uses &Theta;(<em>V</em>) extra space (not including the digraph).
#  *  <p>
#  *  For additional documentation,
#  *  see <a href="https://algs4.cs.princeton.edu/42digraph">Section 4.2</a> of
#  *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
#  *
#  *  @author Robert Sedgewick
#  *  @author Kevin Wayne
#  */
class DepthFirstOrder:
    """Compute preorder and postorder for a digraph or edge-weighted digraph"""
    ## private int preCounter;            // counter or preorder numbering
    ## private int postCounter;           // counter for postorder numbering

    def __init__(self, dag, sort_adj=False):
        self.marked    = [False]* dag.num_vertices
        self.postorder = []                        #           vertices in preorder
        if sort_adj:
            #print('BEFORE:', dag)
            dag = self._sort_dag(dag)
            #print('AFTER: ', dag)
        for v in range(dag.num_vertices):
            if not self.marked[v]:
                self._dfs(dag, v)
        ## self._pre    = new int[dag.V()]         # int[]     preorder  number of v
        ## self._post   = new int[dag.V()]         # int[]     postorder number of v
        ## self._preorder  = new Queue<Integer>()  #           vertices in postorder
        # boolean[] marked[v] = has v been marked in dfs?

        ## assert check()

    def _dfs(self, dag, v):
        """run DFS in digraph dag from vertex v and compute preorder/postorder"""
        self.marked[v] = True
        ## pre[v] = preCounter++
        ## preorder.enqueue(v)
        for w in dag.adj(v):
            if not self.marked[w]:
                self._dfs(dag, w)
        self.postorder.append(v)
        ## post[v] = postCounter++

    ##// run DFS in edge-weighted digraph dag from vertex v and compute preorder/postorder
    ##private void dfs(EdgeWeightedDigraph dag, int v) {
    ##    marked[v] = true
    ##    pre[v] = preCounter++
    ##    preorder.enqueue(v)
    ##    for (DirectedEdge e : dag.adj(v)) {
    ##        int w = e.to()
    ##        if (!marked[w]) {
    ##            dfs(dag, w)
    ##        }
    ##    }
    ##    self.postorder.append(v)
    ##    post[v] = postCounter++
    ##}

    ##/**
    ## * Returns the preorder number of vertex {@code v}.
    ## * @param  v the vertex
    ## * @return the preorder number of vertex {@code v}
    ## * @throws IllegalArgumentException unless {@code 0 <= v < V}
    ## */
    ##public int pre(int v) {
    ##    validateVertex(v)
    ##    return pre[v]
    ##}

    ##/**
    ## * Returns the postorder number of vertex {@code v}.
    ## * @param  v the vertex
    ## * @return the postorder number of vertex {@code v}
    ## * @throws IllegalArgumentException unless {@code 0 <= v < V}
    ## */
    ##public int post(int v) {
    ##    validateVertex(v)
    ##    return post[v]
    ##}

    def get_postorder(self):
        """Get a list of the vertices in reverse postorder"""
        return self.postorder[::]

    ##/**
    ## * Returns the vertices in preorder.
    ## * @return the vertices in preorder, as an iterable of vertices
    ## */
    ##public Iterable<Integer> pre() {
    ##    return preorder
    ##}

    def get_reverse_post(self):  # public Iterable<Integer> reversePost()
        """Get a list of the vertices in reverse postorder"""
        return self.postorder[::-1]

    ##// check that pre() and post() are consistent with pre(v) and post(v)
    ##private boolean check() {

    ##    // check that post(v) is consistent with post()
    ##    int r = 0
    ##    for (int v : post()) {
    ##        if (post(v) != r) {
    ##            StdOut.println("post(v) and post() inconsistent")
    ##            return false
    ##        }
    ##        r++
    ##    }

    ##    // check that pre(v) is consistent with pre()
    ##    r = 0
    ##    for (int v : pre()) {
    ##        if (pre(v) != r) {
    ##            StdOut.println("pre(v) and pre() inconsistent")
    ##            return false
    ##        }
    ##        r++
    ##    }

    ##    return true
    ##}

    ##// throw an IllegalArgumentException unless {@code 0 <= v < V}
    ##private void validateVertex(int v) {
    ##    int V = marked.length
    ##    if (v < 0 || v >= V)
    ##        throw new IllegalArgumentException("vertex " + v + " is not between 0 and " + (V-1))
    ##}

    def _sort_dag(self, dag):
        # pylint: disable=import-outside-toplevel
        from copy import deepcopy
        ret = deepcopy(dag)
        ret.adjs = [sorted(s) for s in ret.adjs]
        #for elem in ret.adjs:
        #    print('AAAAAAAAAAAAAAAAAAAAAAAA', sorted(elem))
        #    ret.append(sorted(elem))
        return ret


# Copyright 2002, Robert Sedgewick and Kevin Wayne.
# Copyright 2026, DV Klopfenstein, PhD, Python port
