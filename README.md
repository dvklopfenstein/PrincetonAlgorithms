Princeton Algorithms
====================

Coursera Princeton Algorithms: Python implementations of selected Algorithms and Clients
from Princeton's Java implementations retreived on July 2014 from: 

  http://algs4.cs.princeton.edu/code/

At some point, I plan to add C++ implementations little-by-little as well...



    1 FUNDAMENTALS                                            DATA
    - ------------------------------------------------------  --------------
  –     BinarySearch.py     binary search                     tinyW.txt tinyT.txt largeW.txt largeT.txt  
  –     RandomSeq.py        random numbers in a given range   –
  –     Average.py          average of a sequence of numbers  –
  –     Cat.py              concatenate files                 in1.txt in2.txt  
  – J   Knuth.py            Knuth shuffle                     cards.txt  
  –     Counter.py          counter                           –
  –     StaticSETofInts.py  set of integers                   –
  –     Whitelist.py        whitelist client                  tinyW.txt tinyT.txt largeW.txt largeT.txt  
  –     Vector.py           Euclidean vector                  –
  – J   Date.py             date                              –
  –     Transaction.py      transaction                       –
  –     Point2D.py          point                             –
  –     Interval1D.py       1d interval                       –
  –     Interval2D.py       2d interval                       –
1.1 J   ResizingArrayStack.py LIFO stack (resizing array)     tobe.txt  
1.2     LinkedStack.py      LIFO stack (linked list)          tobe.txt  
  – J   Stack.py            LIFO stack                        tobe.txt
  – J   ResizingArrayQueue.py FIFO queue (resizing array)     tobe.txt  
1.3     LinkedQueue.py      FIFO queue (linked list)          tobe.txt  
  – J   Queue.py            FIFO queue                        tobe.txt
  – J   ResizingArrayBag.py multiset (resizing array)         –
1.4     LinkedBag.py        multiset (linked list)            –
  – J   Bag.py              multiset                          –
  –     Stopwatch.py        timer (wall time)                 –
  –     StopwatchCPU.py     timer (CPU time)                  –
  –     LinearRegression.py simple linear regression          –
  –     PolynomialRegression.py polynomial regression         –
  –     ThreeSum.py         brute-force three sum             1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
  –     ThreeSumFast.py     faster three sum                  1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt  
  –     DoublingTest.py     doubling test                     –
  –     DoublingRatio.py    doubling ratio                    –
  – J   QuickFindUF.py      quick find                        tinyUF.txt mediumUF.txt largeUF.txt
  –     QuickUnionUF.py     quick union                       tinyUF.txt mediumUF.txt largeUF.txt
1.5 J   WeightedQuickUnionUF.py weighted quick union        tinyUF.txt mediumUF.txt largeUF.txt
  –     UF.py               union-by-rank with path halving   tinyUF.txt mediumUF.txt largeUF.txt

    2 SORTING                                               DATA
    - ----------------------------------------------------  --------------
J   2.1 Insertion.py      insertion sort tiny.txt           words3.txt  
      – InsertionX.py     optimized insertion               sort tiny.txt words3.txt  
J   2.2 Selection.py      selection sort                    –
J   2.3 Shell.py          shellsort                         –
    2.4 Merge.py          top-down mergesort                –
      – MergeBU.py        bottom-up mergesort               –
      – MergeX.py         optimized mergesort               –
    2.5 Quick.py          quicksort                         –
      – Quick3way.py      quicksort with 3-way partitioning –
      – QuickX.py         optimized quicksort               –
      – TopM.py           priority queue client i           tinyBatch.txt
J   2.6 MaxPQ.py          max heap priority queue           tinyPQ.txt
      – MinPQ.py          min heap priority queue           tinyPQ.txt
      – IndexMinPQ.py     index min heap priority queue     –
      – IndexMaxPQ.py     index max heap priority queue     –
      – Multiway.py       multiway merge                    m1.txt m2.txt m3.txt
J   2.7 Heap.py           heapsort                          tiny.txt words3.txt

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
    
    § PROGRAM DESCRIPTION / JAVADOC
J   1.5 StdIn.py read numbers and text from standard input
J   1.5 StdOut.py write numbers and text to standard output
J   1.5 StdDraw.py draw geometric shapes in a window
    1.5 StdAudio.py create, play, and manipulate sound
J   2.2 StdRandom.py generate random numbers
J   2.2 StdStats.py compute statistics
J   2.2 StdArrayIO.py read and write 1D and 2D arrays
    3.1 In.py read numbers and text from files and URLs
    3.1 Out.py write numbers and text to files
    3.1 Draw.py draw geometric shapes
    3.1 Picture.py process digital images
J   3.2 Stopwatch.py measure running time
    – BinaryStdIn.py read bits from standard input
    – BinaryStdOut.py write bits to standard output
    – BinaryIn.py read bits from files and URLs
    – BinaryOut.py write bits to files

Bonus Java Files:
BouncingBalls.java
EvaluatePostfix.java
UnorderedMaxPQ.java

Bonus Python Files:
