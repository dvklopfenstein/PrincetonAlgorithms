Princeton University's "Algorithms and Clients"
===========================================
by Kevin Wayne, Robert Sedgewick
--------------------------------

Implemented in Python 2.7.x by D Klopfenstein is selected code from:

  * http://algs4.cs.princeton.edu/code/

Python implementations contain:
* Additional comments in the code that are based on material from the [coursera class](https://class.coursera.org/algs4partI-006) or
[book](http://smile.amazon.com/Algorithms-4th-Robert-Sedgewick/dp/032157351X/ref=sr_1_1?s=books&ie=UTF8&qid=1410217876&sr=1-1)
* Additional code used for visualization to help me absorb the material

**TESTS**: 
 * **Python** tests are run from: [./py/AlgsSedgewickWayne/tests/](./py/AlgsSedgewickWayne/tests)
 * Some algorithms implemented in Python contain "main" methods and can be run from their local directory: [./py/AlgsSedgewickWayne](./py/AlgsSedgewickWayne)
 * **Java** code is run from: [./thirdparty/](./thirdparty)
   * To download Sedgewick-Wayne Java programming environment: 
     [Linux](http://algs4.cs.princeton.edu/linux/),
     [Windows](http://algs4.cs.princeton.edu/windows/),
     [Mac OS X](http://algs4.cs.princeton.edu/mac/)

**PREREQUISITES**: python, numpy, pylab, matplotlib, math, sys, os.
*NOTE*: Most Python modules in this repository do not use matplotlib or pylab.

**PYTHONPATH**: Add the directory: \<your_directory\>/PrincetonAlgorithms/py/AlgsSedgewickWayne/

**Key:**
* J: Java file downloaded from Princeton Algorithm's "Java Algorithms and Clients"
* P: Python implementation is present
* C: C++ implementation is present


```
Key   1 FUNDAMENTALS         Description                      DATA
:-- --: :------------------- :-----------------------------   :-------------
JP.   – BinarySearch         binary search                    tinyW.txt tinyT.txt largeW.txt largeT.txt
...   – RandomSeq            random numbers in a given range  –
...   – Average              average of a sequence of numbers –
...   – Cat                  concatenate files                in1.txt in2.txt
J..   – Knuth                Knuth shuffle                    cards.txt
...   – Counter              counter                          –
...   – StaticSETofInts      set of integers                  –
...   – Whitelist            whitelist client                 tinyW.txt tinyT.txt largeW.txt largeT.txt
...   – Vector               Euclidean vector                 –
J..   – Date                 date                             –
...   – Transaction          transaction                      –
J..   – Point2D              point                            –
...   – Interval1D           1d interval                      –
...   – Interval2D           2d interval                      –
JP. 1.1 ResizingArrayStack   LIFO stack (resizing array)      tobe.txt
J.. 1.2 LinkedStack          LIFO stack (linked list)         tobe.txt
JP.   – Stack                LIFO stack                       tobe.txt
JP.   – ResizingArrayQueue   FIFO queue (resizing array)      tobe.txt
J.. 1.3 LinkedQueue          FIFO queue (linked list)         tobe.txt
JP.   – Queue                FIFO queue                       tobe.txt
J..   – ResizingArrayBag     multiset (resizing array)        –
J.. 1.4 LinkedBag            multiset (linked list)           –
JP.   – Bag                  multiset                         –
...   – Stopwatch            timer (wall time)                –
...   – StopwatchCPU         timer (CPU time)                 –
...   – LinearRegression     simple linear regression         –
...   – PolynomialRegression polynomial regression            –
JP.   – ThreeSum             brute-force three sum            1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
J..   – ThreeSumFast         faster three sum                 1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
...   – DoublingTest         doubling test                    –
...   – DoublingRatio        doubling ratio                   –
JP.   – QuickFindUF          quick find                       tinyUF.txt mediumUF.txt largeUF.txt
JP.   – QuickUnionUF         quick union                      tinyUF.txt mediumUF.txt largeUF.txt
JP. 1.5 WeightedQuickUnionUF weighted quick union             tinyUF.txt mediumUF.txt largeUF.txt
...  –  UF                   union-by-rank with path halving  tinyUF.txt mediumUF.txt largeUF.txt


Key   2 SORTING     Description                       DATA
:-- --: :---------- :-----------------------------    :-------------
JP. 2.1 Insertion   insertion sort tiny.txt           words3.txt
...   – InsertionX  optimized insertion               sort tiny.txt words3.txt
JP. 2.2 Selection   selection sort                    –
JP. 2.3 Shell       shellsort                         –
JP. 2.4 Merge       top-down mergesort                –
JP.   – MergeBU     bottom-up mergesort               –
JP.   – MergeX      optimized mergesort               –
JP. 2.5 Quick       quicksort                         –
JP.   – Quick3way   quicksort with 3-way partitioning –
JP.   – QuickX      optimized quicksort               –
...   – TopM        priority queue client i           tinyBatch.txt
JP. 2.6 MaxPQ       max heap priority queue           tinyPQ.txt
J..   – MinPQ       min heap priority queue           tinyPQ.txt
...   – IndexMinPQ  index min heap priority queue     –
...   – IndexMaxPQ  index max heap priority queue     –
...   – Multiway    multiway merge                    m1.txt m2.txt m3.txt
J.. 2.7 Heap        heapsort                          tiny.txt words3.txt


Key   3 SEARCHING              Description                  DATA
:-- --: ---------------------- :--------------------------  :-------------
...   – FrequencyCounter       frequency counter            tinyTale.txt tale.txt leipzig1M.txt
... 3.1 SequentialSearchST     sequential search            tinyST.txt
... 3.2 BinarySearchST         binary search                tinyST.txt
J.. 3.3 BST binary             search tree                  tinyST.txt
... 3.4 RedBlackBST red-black  tree                         tinyST.txt
... 3.5 SeparateChainingHashST separate chaining hash table –
... 3.6 LinearProbingHashST    linear probing hash table    –
J..   – ST                     ordered symbol table         –
...   – SET                    ordered set                  –
...   – DeDup                  remove duplicates            tinyTale.txt
...   – WhiteFilter            whitelist filter             list.txt tinyTale.txt
...   – BlackFilter            blacklist filter             list.txt tinyTale.txt
...   – LookupCSV              dictionary lookup            ip.csv  DJIA.csv  amino.csv  UPC.csv
...   – LookupIndex            index and inverted index     aminoI.csv movies.txt
...   – FileIndex              file indexing                ex1.txt ex2.txt ex3.txt ex4.txt
...   – SparseVector           sparse vector                –


Key    4 GRAPHS                    Description                         DATA
:-- ---: :------------------------ :---------------------------------- :---------------------
...    – Graph                     undirected graph                    tinyG.txt mediumG.txt
...    – GraphGenerator            generate random graphs              –
...    – DepthFirstSearch          depth-first search in a graph       tinyG.txt mediumG.txt
...  4.1 DepthFirstPaths           paths in a graph (DFS)              tinyCG.txt mediumG.txt largeG.txt
...  4.2 BreadthFirstPaths         paths in a graph (BFS)              tinyCG.txt mediumG.txt largeG.txt
...  4.3 CC                        connected components of a graph     tinyG.txt mediumG.txt largeG.txt
...    – Bipartite                 bipartite or odd cycle              –
...    – Cycle                     cycle in a graph                    tinyG.txt mediumG.txt largeG.txt
...    – SymbolGraph               symbol graph                        routes.txt movies.txt
...    – DegreesOfSeparation       degrees of separation               routes.txt movies.txt
...    – Digraph                   directed graph                      tinyDG.txt
...    – DigraphGenerator          generate random digraphs            –
...  4.4 DirectedDFS               depth-first search in a digraph     tinyDG.txt
...    – DepthFirstDirectedPaths   paths in a digraph (DFS)            tinyDG.txt mediumDG.txt
...    – DirectedCycle             cycle in a digraph                  tinyDG.txt tinyDAG.txt
...    – DepthFirstOrder           depth-first order in a digraph      tinyDG.txt tinyDAG.txt
...  4.5 Topological               topological order in a DAG          jobs.txt
...    – BreadthFirstDirectedPaths paths in a digraph (BFS)            tinyDG.txt mediumDG.txt
...    – TransitiveClosure         transitive closure                  tinyDG.txt
...    – SymbolDigraph             symbol digraph                      –
...  4.6 KosarajuSharirSCC         strong components (Kosaraju-Sharir) tinyDG.txt mediumDG.txt largeDG.txt
...    – TarjanSCC                 strong components (Tarjan)          tinyDG.txt mediumDG.txt largeDG.txt
...    – GabowSCC                  strong components (Gabow)           tinyDG.txt mediumDG.txt largeDG.txt
...    – EdgeWeightedGraph         edge-weighted graph                 –
...    – Edge                      weighted edge                       –
...    – LazyPrimMST               MST (lazy Prim)                     tinyEWG.txt mediumEWG.txt largeEWG.txt
...  4.7 PrimMST                   MST (Prim)                          tinyEWG.txt mediumEWG.txt largeEWG.txt
...  4.8 KruskalMST                MST (Kruskal)                       tinyEWG.txt mediumEWG.txt largeEWG.txt
...    – BoruvkaMST                MST (Boruvka)                       tinyEWG.txt mediumEWG.txt largeEWG.txt
...    – EdgeWeightedDigraph       edge-weighted digraph               tinyEWD.txt
...    – DirectedEdge              weighted, directed edge             –
...  4.9 DijkstraSP                shortest paths (Dijkstra)           tinyEWD.txt mediumEWD.txt largeEWD.txt
...    – DijkstraAllPairsSP        all-pairs shortest paths            tinyEWD.txt mediumEWD.txt
... 4.10 AcyclicSP                 shortest paths in a DAG             tinyEWDAG.txt
...    – AcyclicLP                 longest paths in a DAG              tinyEWDAG.txt
...    – CPM                       critical path method                jobsPC.txt
... 4.11 BellmanFordSP             shortest paths (Bellman-Ford)       tinyEWDn.txt tinyEWDnc.txt
...    – EdgeWeightedDirectedCycle cycle in an edge-weighted digraph   –
...    – Arbitrage                 arbitrage detection                 rates.txt
...    – FloydWarshall             all-pairs shortest paths (dense)    tinyEWD.txt mediumEWD.txt
...    – AdjMatrixEdgeWeightedDigraph edge-weighted graph (dense)      tinyEWD.txt


Key    5 STRINGS      Description                         DATA
:-- ---: :----------- :---------------------------------- :---------------------
...    – Alphabet     alphabet                            –
...    – Count        alphabet client                     abra.txt pi.txt
...  5.1 LSD          LSD radix sort                      words3.txt
...  5.2 MSD          MSD radix sort                      shells.txt
...  5.3 Quick3string 3-way string quicksort              shells.txt
...  5.4 TrieST       multiway trie symbol table          shellsST.txt
...    – TrieSET      multiway trie set                   shellsST.txt
...  5.5 TST          ternary search trie                 shellsST.txt
...  5.6 KMP          Knuth-Morris-Pratt substring search –
...  5.7 BoyerMoore   Boyer-Moore substring search        –
...  5.8 RabinKarp    Rabin-Karp substring search         –
...  5.9 NFA          NFA for regular expressions         –
...    – GREP         grep                                –
...    – BinaryDump   binary dump                         abra.txt
...    – HexDump      hex dump                            abra.txt
...    – PictureDump  picture dump                        abra.txt
...    – Genome       genomic code                        genomeTiny.txt genomeVirus.txt
...    – RunLength    run-length coding                   4runs.bin q32x48.bin q64x96.bin
... 5.10 Huffman      Huffman coding                      tinytinyTale.txt medTale.txt tale.txt
... 5.11 LZW          Lempel-Ziv-Welch coding             abraLZW.txt ababLZW.txt


Key   6 CONTEXT                Description                 DATA
:-- --: :--------------------- :-------------------------- :---------------------
... 6.1 CollisionSystem        collision system            brownian.txt diffusion.txt
...   – Particle               particle                    –
... 6.2 BTree                  B-tree                      –
... 6.3 SuffixArray            suffix array                abra.txt
...   – SuffixArrayX           suffix array                abra.txt
...   – LRS                    longest repeated substring  tinyTale.txt mobydick.txt
...   – KWIK                   keyword in context          tale.txt
...   – LongestCommonSubstring longest common substring    tale.txt mobydick.txt
... 6.4 FordFulkerson          max flow / min cut          tinyFN.txt
...   – FlowNetwork            capacitated network         –
...   – FlowEdge               capacitated edge with flow  –
...   – BipartiteMatching      bipartite matching          –
...   – AssignmentProblem      weighted bipartite matching –
...   – Simplex                simplex method              –


Key   9 BEYOND              Description            DATA
:-- --: :------------------ :--------------------- :---------------------
...   – GaussianElimination Gaussian elimination   –
...   – FFT                 Fast Fourier transform –
...   – Complex             complex number         –
J..   – GrahamScan          2d convex hull         rs1423.txt kw1260.txt
...   – FarthestPair        2d farthest pair       rs1423.txt kw1260.txt
...   – ClosestPair         2d closest pair        rs1423.txt kw1260.txt


Standard input and output libraries. We use these standard
input and output libraries from Introduction to Programming:
An Interdisciplinary Approach. You can download them all
together as stdlib.jar.

Key   § PROGRAM      DESCRIPTION / JAVADOC
:-- --: :----------- :----------------------------------------
J.. 1.5 StdIn        read numbers and text from standard input
J.. 1.5 StdOut       write numbers and text to standard output
J.. 1.5 StdDraw      draw geometric shapes in a window
... 1.5 StdAudio     create, play, and manipulate sound
J.. 2.2 StdRandom    generate random numbers
J.. 2.2 StdStats     compute statistics
J.. 2.2 StdArrayIO   read and write 1D and 2D arrays
... 3.1 In           read numbers and text from files and URLs
... 3.1 Out          write numbers and text to files
... 3.1 Draw         draw geometric shapes
... 3.1 Picture      process digital images
J.. 3.2 Stopwatch    measure running time
...   – BinaryStdIn  read bits from standard input
...   – BinaryStdOut write bits to standard output
...   – BinaryIn     read bits from files and URLs
...   – BinaryOut    write bits to files
```

Additional Java Files:
* BouncingBalls.java
* EvaluatePostfix.java
* UnorderedMaxPQ.java

Additional Python Files:
