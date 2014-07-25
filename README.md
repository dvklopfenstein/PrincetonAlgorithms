Princeton University Algorithms and Clients
===========================================
by Kevin Wayne, Robert Sedgewick
--------------------------------

Implemented in Python 2.7 by D Klopfenstein are selected code from this link:

  http://algs4.cs.princeton.edu/code/

At some point, I plan to add C++ implementations little-by-little when needed as well...

**Key:**
* J: Java file downloaded from Princeton Algorithm's "Java Algorithms and Clients"
* P: Python implementation is present
* C: C++ implementaion is present


```
Key   1 FUNDAMENTALS         Description                      DATA
:-- ---::------------------- :-----------------------------   :-------------
      – BinarySearch         binary search                    tinyW.txt tinyT.txt largeW.txt largeT.txt  
      – RandomSeq            random numbers in a given range  –
      – Average              average of a sequence of numbers –
      – Cat                  concatenate files                in1.txt in2.txt  
J     – Knuth                Knuth shuffle                    cards.txt  
      – Counter              counter                          –
      – StaticSETofInts      set of integers                  –
      – Whitelist            whitelist client                 tinyW.txt tinyT.txt largeW.txt largeT.txt  
      – Vector               Euclidean vector                 –
J     – Date                 date                             –
      – Transaction          transaction                      –
      – Point2D              point                            –
      – Interval1D           1d interval                      –
      – Interval2D           2d interval                      –
J   1.1 ResizingArrayStack   LIFO stack (resizing array)      tobe.txt  
    1.2 LinkedStack          LIFO stack (linked list)         tobe.txt  
J     – Stack                LIFO stack                       tobe.txt
J     – ResizingArrayQueue   FIFO queue (resizing array)      tobe.txt  
    1.3 LinkedQueue          FIFO queue (linked list)         tobe.txt  
J     – Queue                FIFO queue                       tobe.txt
J     – ResizingArrayBag     multiset (resizing array)        –
    1.4 LinkedBag            multiset (linked list)           –
J     – Bag                  multiset                         –
      – Stopwatch            timer (wall time)                –
      – StopwatchCPU         timer (CPU time)                 –
      – LinearRegression     simple linear regression         –
      – PolynomialRegression polynomial regression            –
      – ThreeSum             brute-force three sum            1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
      – ThreeSumFast         faster three sum                 1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt  
      – DoublingTest         doubling test                    –
      – DoublingRatio        doubling ratio                   –
J     – QuickFindUF          quick find                       tinyUF.txt mediumUF.txt largeUF.txt
      – QuickUnionUF         quick union                      tinyUF.txt mediumUF.txt largeUF.txt
J   1.5 WeightedQuickUnionUF weighted quick union             tinyUF.txt mediumUF.txt largeUF.txt
     –  UF                   union-by-rank with path halving  tinyUF.txt mediumUF.txt largeUF.txt


Key   2 SORTING     Description                       DATA
:-- ---::---------- :-----------------------------    :-------------
J   2.1 Insertion   insertion sort tiny.txt           words3.txt  
      – InsertionX  optimized insertion               sort tiny.txt words3.txt  
J   2.2 Selection   selection sort                    –
J   2.3 Shell       shellsort                         –
    2.4 Merge       top-down mergesort                –
      – MergeBU     bottom-up mergesort               –
      – MergeX      optimized mergesort               –
    2.5 Quick       quicksort                         –
      – Quick3way   quicksort with 3-way partitioning –
      – QuickX      optimized quicksort               –
      – TopM        priority queue client i           tinyBatch.txt
J   2.6 MaxPQ       max heap priority queue           tinyPQ.txt
      – MinPQ       min heap priority queue           tinyPQ.txt
      – IndexMinPQ  index min heap priority queue     –
      – IndexMaxPQ  index max heap priority queue     –
      – Multiway    multiway merge                    m1.txt m2.txt m3.txt
J   2.7 Heap        heapsort                          tiny.txt words3.txt

    3 SEARCHING DATA
    - ----------------------------------------------------  --------------
    – FrequencyCounter.py frequency counter tinyTale.txt  tale.txt  leipzig1M.txt  
    3.1 SequentialSearchST.py sequential search tinyST.txt  
    3.2 BinarySearchST.py binary search tinyST.txt  
    3.3 BST.py binary search tree tinyST.txt  
    3.4 RedBlackBST.py red-black tree tinyST.txt  
    3.5 SeparateChainingHashST.py separate chaining hash table –
    3.6 LinearProbingHashST.py linear probing hash table –
J   – ST.py ordered symbol table –
    – SET.py ordered set –
    – DeDup.py remove duplicates tinyTale.txt  
    – WhiteFilter.py whitelist filter list.txt  tinyTale.txt  
    – BlackFilter.py blacklist filter list.txt  tinyTale.txt  
    – LookupCSV.py dictionary lookup ip.csv  DJIA.csv  amino.csv  UPC.csv  
    – LookupIndex.py index and inverted index aminoI.csv  movies.txt  
    – FileIndex.py file indexing ex1.txt  ex2.txt  ex3.txt  ex4.txt  
    – SparseVector.py sparse vector –

    4 GRAPHS DATA
    - ----------------------------------------------------  --------------
    – Graph.py undirected graph tinyG.txt  mediumG.txt  
    – GraphGenerator.py generate random graphs –
    – DepthFirstSearch.py depth-first search in a graph tinyG.txt  mediumG.txt  
    4.1 DepthFirstPaths.py paths in a graph (DFS) tinyCG.txt  mediumG.txt  largeG.txt  
    4.2 BreadthFirstPaths.py paths in a graph (BFS) tinyCG.txt  mediumG.txt  largeG.txt  
    4.3 CC.py connected components of a graph tinyG.txt  mediumG.txt  largeG.txt  
    – Bipartite.py bipartite or odd cycle –
    – Cycle.py cycle in a graph tinyG.txt  mediumG.txt  largeG.txt  
    – SymbolGraph.py symbol graph routes.txt  movies.txt  
    – DegreesOfSeparation.py degrees of separation routes.txt  movies.txt  
    – Digraph.py directed graph tinyDG.txt  
    – DigraphGenerator.py generate random digraphs –
    4.4 DirectedDFS.py depth-first search in a digraph tinyDG.txt  
    – DepthFirstDirectedPaths.py paths in a digraph (DFS) tinyDG.txt  mediumDG.txt  
    – DirectedCycle.py cycle in a digraph tinyDG.txt  tinyDAG.txt  
    – DepthFirstOrder.py depth-first order in a digraph tinyDG.txt  tinyDAG.txt  
    4.5 Topological.py topological order in a DAG jobs.txt  
    – BreadthFirstDirectedPaths.py paths in a digraph (BFS) tinyDG.txt  mediumDG.txt  
    – TransitiveClosure.py transitive closure tinyDG.txt  
    – SymbolDigraph.py symbol digraph –
    4.6 KosarajuSharirSCC.py strong components (Kosaraju-Sharir) tinyDG.txt  mediumDG.txt  largeDG.txt  
    – TarjanSCC.py strong components (Tarjan) tinyDG.txt  mediumDG.txt  largeDG.txt  
    – GabowSCC.py strong components (Gabow) tinyDG.txt  mediumDG.txt  largeDG.txt  
    – EdgeWeightedGraph.py edge-weighted graph –
    – Edge.py weighted edge –
    – LazyPrimMST.py MST (lazy Prim) tinyEWG.txt  mediumEWG.txt  largeEWG.txt  
    4.7 PrimMST.py MST (Prim) tinyEWG.txt  mediumEWG.txt  largeEWG.txt  
    4.8 KruskalMST.py MST (Kruskal) tinyEWG.txt  mediumEWG.txt  largeEWG.txt  
    – BoruvkaMST.py MST (Boruvka) tinyEWG.txt  mediumEWG.txt  largeEWG.txt  
    – EdgeWeightedDigraph.py edge-weighted digraph tinyEWD.txt  
    – DirectedEdge.py weighted, directed edge –
    4.9 DijkstraSP.py shortest paths (Dijkstra) tinyEWD.txt  mediumEWD.txt  largeEWD.txt  
    – DijkstraAllPairsSP.py all-pairs shortest paths tinyEWD.txt  mediumEWD.txt  
    4.10 AcyclicSP.py shortest paths in a DAG tinyEWDAG.txt  
    – AcyclicLP.py longest paths in a DAG tinyEWDAG.txt  
    – CPM.py critical path method jobsPC.txt  
    4.11 BellmanFordSP.py shortest paths (Bellman-Ford) tinyEWDn.txt  tinyEWDnc.txt  
    – EdgeWeightedDirectedCycle.py cycle in an edge-weighted digraph –
    – Arbitrage.py arbitrage detection rates.txt  
    – FloydWarshall.py all-pairs shortest paths (dense) tinyEWD.txt  mediumEWD.txt  
    – AdjMatrixEdgeWeightedDigraph.py edge-weighted graph (dense) tinyEWD.txt  
    5 STRINGS DATA
    – Alphabet.py alphabet –
    – Count.py alphabet client abra.txt  pi.txt  
    5.1 LSD.py LSD radix sort words3.txt  
    5.2 MSD.py MSD radix sort shells.txt  
    5.3 Quick3string.py 3-way string quicksort shells.txt  
    5.4 TrieST.py multiway trie symbol table shellsST.txt  
    – TrieSET.py multiway trie set shellsST.txt  
    5.5 TST.py ternary search trie shellsST.txt  
    5.6 KMP.py Knuth-Morris-Pratt substring search –
    5.7 BoyerMoore.py Boyer-Moore substring search –
    5.8 RabinKarp.py Rabin-Karp substring search –
    5.9 NFA.py NFA for regular expressions –
    – GREP.py grep –
    – BinaryDump.py binary dump abra.txt  
    – HexDump.py hex dump abra.txt  
    – PictureDump.py picture dump abra.txt  
    – Genome.py genomic code genomeTiny.txt  genomeVirus.txt  
    – RunLength.py run-length coding 4runs.bin  q32x48.bin  q64x96.bin  
    5.10 Huffman.py Huffman coding tinytinyTale.txt  medTale.txt  tale.txt  
    5.11 LZW.py Lempel-Ziv-Welch coding abraLZW.txt  ababLZW.txt  
    6 CONTEXT DATA
    6.1 CollisionSystem.py collision system brownian.txt  diffusion.txt  
    – Particle.py particle –
    6.2 BTree.py B-tree –
    6.3 SuffixArray.py suffix array abra.txt  
    – SuffixArrayX.py suffix array abra.txt  
    – LRS.py longest repeated substring tinyTale.txt  mobydick.txt  
    – KWIK.py keyword in context tale.txt  
    – LongestCommonSubstring.py longest common substring tale.txt  mobydick.txt  
    6.4 FordFulkerson.py max flow / min cut tinyFN.txt  
    – FlowNetwork.py capacitated network –
    – FlowEdge.py capacitated edge with flow –
    – BipartiteMatching.py bipartite matching –
    – AssignmentProblem.py weighted bipartite matching –
    – Simplex.py simplex method –
    9 BEYOND DATA
    – GaussianElimination.py Gaussian elimination –
    – FFT.py Fast Fourier transform –
    – Complex.py complex number –
    – GrahamScan.py 2d convex hull rs1423.txt  kw1260.txt  
    – FarthestPair.py 2d farthest pair rs1423.txt  kw1260.txt  
    – ClosestPair.py 2d closest pair rs1423.txt  kw1260.txt  
    
    
    Standard input and output libraries. We use these standard input and output libraries from Introduction to Programming: An Interdisciplinary Approach. You can download them all together as stdlib.jar.
    
Key § PROGRAM DESCRIPTION / JAVADOC
:-- ---::---------------------- :-----------------------------   :-------------
J   1.5 StdIn        read numbers and text from standard input
J   1.5 StdOut       write numbers and text to standard output
J   1.5 StdDraw      draw geometric shapes in a window
    1.5 StdAudio     create, play, and manipulate sound
J   2.2 StdRandom    generate random numbers
J   2.2 StdStats     compute statistics
J   2.2 StdArrayIO   read and write 1D and 2D arrays
    3.1 In           read numbers and text from files and URLs
    3.1 Out          write numbers and text to files
    3.1 Draw         draw geometric shapes
    3.1 Picture      process digital images
J   3.2 Stopwatch    measure running time
      – BinaryStdIn  read bits from standard input
      – BinaryStdOut write bits to standard output
      – BinaryIn     read bits from files and URLs
      – BinaryOut    write bits to files
```

Bonus Java Files:
BouncingBalls.java
EvaluatePostfix.java
UnorderedMaxPQ.java

Bonus Python Files:
