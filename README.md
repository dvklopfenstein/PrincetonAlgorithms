# [Princeton University's "Algorithms and Clients"](doc/README.md)
## by Robert Sedgewick, Kevin Wayne
  
Implemented in Python by DV Klopfenstein is selected code from:

  * http://algs4.cs.princeton.edu/code
  * [Java Code in Kevin Wayne's github repository](https://github.com/kevin-wayne/algs4/tree/master/src/main/java/edu/princeton/cs/algs4)

[**Python implementations**](./py/AlgsSedgewickWayne/) contain:
* Additional code used for visualization to help absorb the material
* Additional comments in the code that are based on material from the:    
  * [**book**](http://smile.amazon.com/Algorithms-4th-Robert-Sedgewick/dp/032157351X/ref=sr_1_1?s=books&ie=UTF8&qid=1410217876&sr=1-1)    
  * [**book with lectures**](http://www.amazon.com/Algorithms-Deluxe-Book-24-part-Lecture/dp/0134384687/ref=sr_1_1?s=books&ie=UTF8&qid=1443006543&sr=1-1&keywords=algorithms+deluxe)    
  * [**Kevin Wayne's github**](https://github.com/kevin-wayne/algs4)
  * [**booksite**](http://algs4.cs.princeton.edu/home/)    
  * [**coursera class**](https://www.coursera.org/course/algs4partI)    
  * [**Sound of Sorting**](http://panthema.net/2013/sound-of-sorting/) by [Timo Bingmann](https://github.com/bingmann)

[**TESTS**](doc/README.md): 
 * **Python** tests are run from: [./tests/](./tests)
 * **Java** code is run from: [./thirdparty/](./thirdparty)
   * To download Sedgewick-Wayne Java programming environment: 
     [Linux](http://algs4.cs.princeton.edu/linux/),
     [Windows](http://algs4.cs.princeton.edu/windows/),
     [Mac OS X](http://algs4.cs.princeton.edu/mac/)

**PREREQUISITES**: python, numpy, pylab, math, sys, os.    
*NOTE*: Most Python modules in this repository do not use pylab.

**PYTHONPATH**: Add the directory: \<your_directory\>/PrincetonAlgorithms/py/AlgsSedgewickWayne/

Download Princeton Algorithm's 
["Java Algorithms and Clients"](http://algs4.cs.princeton.edu/code/) 
from [**Kevin Wayne's github**](https://github.com/kevin-wayne/algs4)

**Key:**
* P: Python implementation is present

```
Key  1 FUNDAMENTALS         Description                      DATA
:- --: :------------------- :-----------------------------   :-------------
 P   – BinarySearch         binary search                    tinyW.txt tinyT.txt largeW.txt largeT.txt
 .   – RandomSeq            random numbers in a given range  –
 .   – Average              average of a sequence of numbers –
 .   – Cat                  concatenate files                in1.txt in2.txt
 P   – Knuth                Knuth shuffle                    cards.txt
 .   – Counter              counter                          –
 .   – StaticSETofInts      set of integers                  –
 .   – Whitelist            whitelist client                 tinyW.txt tinyT.txt largeW.txt largeT.txt
 .   – Vector               Euclidean vector                 –
 P   – Date                 date                             –
 P   – Transaction          transaction                      –
 .   – Point2D              point                            –
 .   – Interval1D           1d interval                      –
 .   – Interval2D           2d interval                      –
 P 1.1 ResizingArrayStack   LIFO stack (resizing array)      tobe.txt
 . 1.2 LinkedStack          LIFO stack (linked list)         tobe.txt
 P   – Stack                LIFO stack                       tobe.txt
 P   – ResizingArrayQueue   FIFO queue (resizing array)      tobe.txt
 . 1.3 LinkedQueue          FIFO queue (linked list)         tobe.txt
 P   – Queue                FIFO queue                       tobe.txt
 .   – ResizingArrayBag     multiset (resizing array)        –
 . 1.4 LinkedBag            multiset (linked list)           –
 P   – Bag                  multiset                         –
 .   – Stopwatch            timer (wall time)                –
 .   – StopwatchCPU         timer (CPU time)                 –
 .   – LinearRegression     simple linear regression         –
 .   – PolynomialRegression polynomial regression            –
 P   – ThreeSum             brute-force three sum            1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
 .   – ThreeSumFast         faster three sum                 1Kints.txt 2Kints.txt 4Kints.txt 8Kints.txt
 .   – DoublingTest         doubling test                    –
 .   – DoublingRatio        doubling ratio                   –
 P   – QuickFindUF          quick find                       tinyUF.txt mediumUF.txt largeUF.txt
 P   – QuickUnionUF         quick union                      tinyUF.txt mediumUF.txt largeUF.txt
 P 1.5 WeightedQuickUnionUF weighted quick union             tinyUF.txt mediumUF.txt largeUF.txt
 P   - WeightedQuickUnionUFPlus weighted quick union w/path compression        
 .   - UF                   union-by-rank with path halving  tinyUF.txt mediumUF.txt largeUF.txt


Key  2 SORTING     Description                       DATA
 - --: :---------- :-----------------------------    :-------------
 P 2.1 Insertion   insertion sort tiny.txt           words3.txt
 .   – InsertionX  optimized insertion               sort tiny.txt words3.txt
 P 2.2 Selection   selection sort                    –
 P 2.3 Shell       shellsort                         –
 P 2.4 Merge       top-down mergesort                –
 P   – MergeBU     bottom-up mergesort               –
 P   – MergeX      optimized mergesort               –
 P 2.5 Quick       quicksort                         –
 P   – Quick3way   quicksort with 3-way partitioning –
 P   – QuickX      optimized quicksort               –
 P   – TopM        priority queue client i           tinyBatch.txt
 P 2.6 MaxPQ       max heap priority queue           tinyPQ.txt
 .   – MinPQ       min heap priority queue           tinyPQ.txt
 .   – IndexMinPQ  index min heap priority queue     –
 .   – IndexMaxPQ  index max heap priority queue     –
 .   – Multiway    multiway merge                    m1.txt m2.txt m3.txt
 P 2.7 Heap        heapsort                          tiny.txt words3.txt


Key  3 SEARCHING              Description                  DATA
 - --: ---------------------- :--------------------------  :-------------
 .   – FrequencyCounter       frequency counter            tinyTale.txt tale.txt leipzig1M.txt
 P 3.1 SequentialSearchST     sequential search            tinyST.txt
 . 3.2 BinarySearchST         binary search                tinyST.txt
 . 3.3 BST binary             search tree                  tinyST.txt
 . 3.4 RedBlackBST red-black  tree                         tinyST.txt
 P 3.5 SeparateChainingHashST separate chaining hash table –
 P 3.6 LinearProbingHashST    linear probing hash table    –
 .   – ST                     ordered symbol table         –
 p   – SET                    ordered set                  –
 .   – DeDup                  remove duplicates            tinyTale.txt
 p   – WhiteFilter            whitelist filter             list.txt tinyTale.txt
 .   – BlackFilter            blacklist filter             list.txt tinyTale.txt
 p   – LookupCSV              dictionary lookup            ip.csv  DJIA.csv  amino.csv  UPC.csv
 .   – LookupIndex            index and inverted index     aminoI.csv movies.txt
 .   – FileIndex              file indexing                ex1.txt ex2.txt ex3.txt ex4.txt
 p   – SparseVector           sparse vector                –


Key   4 GRAPHS                    Description                         DATA
 - ---: :------------------------ :---------------------------------- :---------------------
 P    – Graph                     undirected graph                    tinyG.txt mediumG.txt
 .    – GraphGenerator            generate random graphs              –
 .    – DepthFirstSearch          depth-first search in a graph       tinyG.txt mediumG.txt
 P  4.1 DepthFirstPaths           paths in a graph (DFS)              tinyCG.txt mediumG.txt largeG.txt
 P  4.2 BreadthFirstPaths         paths in a graph (BFS)              tinyCG.txt mediumG.txt largeG.txt
 .  4.3 CC                        connected components of a graph     tinyG.txt mediumG.txt largeG.txt
 .    – Bipartite                 bipartite or odd cycle              –
 .    – Cycle                     cycle in a graph                    tinyG.txt mediumG.txt largeG.txt
 .    – SymbolGraph               symbol graph                        routes.txt movies.txt
 .    – DegreesOfSeparation       degrees of separation               routes.txt movies.txt
 P    – Digraph                   directed graph                      tinyDG.txt
 .    – DigraphGenerator          generate random digraphs            –
 p  4.4 DirectedDFS               depth-first search in a digraph     tinyDG.txt
 p    – DepthFirstDirectedPaths   paths in a digraph (DFS)            tinyDG.txt mediumDG.txt
 .    – DirectedCycle             cycle in a digraph                  tinyDG.txt tinyDAG.txt
 .    – DepthFirstOrder           depth-first order in a digraph      tinyDG.txt tinyDAG.txt
 p  4.5 Topological               topological order in a DAG          jobs.txt
 .    – BreadthFirstDirectedPaths paths in a digraph (BFS)            tinyDG.txt mediumDG.txt
 .    – TransitiveClosure         transitive closure                  tinyDG.txt
 .    – SymbolDigraph             symbol digraph                      –
 p  4.6 KosarajuSharirSCC         strong components (Kosaraju-Sharir) tinyDG.txt mediumDG.txt largeDG.txt
 p    – TarjanSCC                 strong components (Tarjan)          tinyDG.txt mediumDG.txt largeDG.txt
 p    – GabowSCC                  strong components (Gabow)           tinyDG.txt mediumDG.txt largeDG.txt
 p    – EdgeWeightedGraph         edge-weighted graph                 –
 P    – Edge                      weighted edge                       –
 p    – LazyPrimMST               MST (lazy Prim)                     tinyEWG.txt mediumEWG.txt largeEWG.txt
 p  4.7 PrimMST                   MST (Prim)                          tinyEWG.txt mediumEWG.txt largeEWG.txt
 p  4.8 KruskalMST                MST (Kruskal)                       tinyEWG.txt mediumEWG.txt largeEWG.txt
 .    – BoruvkaMST                MST (Boruvka)                       tinyEWG.txt mediumEWG.txt largeEWG.txt
 .    – EdgeWeightedDigraph       edge-weighted digraph               tinyEWD.txt
 p    – DirectedEdge              weighted, directed edge             –
 p  4.9 DijkstraSP                shortest paths (Dijkstra)           tinyEWD.txt mediumEWD.txt largeEWD.txt
 .    – DijkstraAllPairsSP        all-pairs shortest paths            tinyEWD.txt mediumEWD.txt
 p 4.10 AcyclicSP                 shortest paths in a DAG             tinyEWDAG.txt
 .    – AcyclicLP                 longest paths in a DAG              tinyEWDAG.txt
 .    – CPM                       critical path method                jobsPC.txt
 p 4.11 BellmanFordSP             shortest paths (Bellman-Ford)       tinyEWDn.txt tinyEWDnc.txt
 p    – EdgeWeightedDirectedCycle cycle in an edge-weighted digraph   –
 .    – Arbitrage                 arbitrage detection                 rates.txt
 .    – FloydWarshall             all-pairs shortest paths (dense)    tinyEWD.txt mediumEWD.txt
 .    – AdjMatrixEdgeWeightedDigraph edge-weighted graph (dense)      tinyEWD.txt


 ey   5 STRINGS      Description                         DATA
 - ---: :----------- :---------------------------------- :---------------------
 .    – Alphabet     alphabet                            –
 .    – Count        alphabet client                     abra.txt pi.txt
 p  5.1 LSD          LSD radix sort                      words3.txt
 p  5.2 MSD          MSD radix sort                      shells.txt
 .  5.3 Quick3string 3-way string quicksort              shells.txt
 p  5.4 TrieST       multiway trie symbol table          shellsST.txt
 .    – TrieSET      multiway trie set                   shellsST.txt
 p  5.5 TST          ternary search trie                 shellsST.txt
 p  5.6 KMP          Knuth-Morris-Pratt substring search –
 p  5.7 BoyerMoore   Boyer-Moore substring search        –
 p  5.8 RabinKarp    Rabin-Karp substring search         –
 p  5.9 NFA          NFA for regular expressions         –
 p    – GREP         grep                                –
 .    – BinaryDump   binary dump                         abra.txt
 .    – HexDump      hex dump                            abra.txt
 .    – PictureDump  picture dump                        abra.txt
 .    – Genome       genomic code                        genomeTiny.txt genomeVirus.txt
 .    – RunLength    run-length coding                   4runs.bin q32x48.bin q64x96.bin
 . 5.10 Huffman      Huffman coding                      tinytinyTale.txt medTale.txt tale.txt
 . 5.11 LZW          Lempel-Ziv-Welch coding             abraLZW.txt ababLZW.txt


 ey  6 CONTEXT                Description                 DATA
 - --: :--------------------- :-------------------------- :---------------------
 . 6.1 CollisionSystem        collision system            brownian.txt diffusion.txt
 .   – Particle               particle                    –
 . 6.2 BTree                  B-tree                      –
 . 6.3 SuffixArray            suffix array                abra.txt
 .   – SuffixArrayX           suffix array                abra.txt
 .   – LRS                    longest repeated substring  tinyTale.txt mobydick.txt
 .   – KWIK                   keyword in context          tale.txt
 .   – LongestCommonSubstring longest common substring    tale.txt mobydick.txt
 p 6.4 FordFulkerson          max flow / min cut          tinyFN.txt
 P   – FlowNetwork            capacitated network         –
 p   – FlowEdge               capacitated edge with flow  –
 .   – BipartiteMatching      bipartite matching          –
 .   – AssignmentProblem      weighted bipartite matching –
 .   – Simplex                simplex method              –


 ey  9 BEYOND              Description            DATA
 - --: :------------------ :--------------------- :---------------------
 .   – GaussianElimination Gaussian elimination   –
 .   – FFT                 Fast Fourier transform –
 .   – Complex             complex number         –
 .   – GrahamScan          2d convex hull         rs1423.txt kw1260.txt
 .   – FarthestPair        2d farthest pair       rs1423.txt kw1260.txt
 .   – ClosestPair         2d closest pair        rs1423.txt kw1260.txt


 tandard input and output libraries. We use these standard
 nput and output libraries from Introduction to Programming:
 n Interdisciplinary Approach. You can download them all
 oether as stdlib.jar.

 ey  § PROGRAM      DESCRIPTION / JAVADOC
 - --: :----------- :----------------------------------------
 . 1.5 StdIn        read numbers and text from standard input
 . 1.5 StdOut       write numbers and text to standard output
 . 1.5 StdDraw      draw geometric shapes in a window
 . 1.5 StdAudio     create, play, and manipulate sound
 . 2.2 StdRandom    generate random numbers
 . 2.2 StdStats     compute statistics
 . 2.2 StdArrayIO   read and write 1D and 2D arrays
 . 3.1 In           read numbers and text from files and URLs
 . 3.1 Out          write numbers and text to files
 . 3.1 Draw         draw geometric shapes
 . 3.1 Picture      process digital images
 . 3.2 Stopwatch    measure running time
 .   – BinaryStdIn  read bits from standard input
 .   – BinaryStdOut write bits to standard output
 .   – BinaryIn     read bits from files and URLs
 .   – BinaryOut    write bits to files
```

Additional Java Files:
* BouncingBalls.java
* EvaluatePostfix.java
* UnorderedMaxPQ.java
* [FileSorter.java](./thirdparty/FileSorter.java)

### License and Copyright
Java code is Copyright © 2002–2016 Robert Sedgewick and Kevin Wayne.  All rights reserved. 
It has a GPLv3 license <http://algs4.cs.princeton.edu/faq/> 
Translation of software from one language to another falls 
under the copyright and license of the original authors. 
It adds a copyright for the translation which is subordinate to the original.

Python translation Copyright © 2014-2016 DV Klopfenstein. All rights reserved.

### Disclaimer of Warranties.
DV Klopfenstein disclaims to the fullest extent authorized by law 
any and all other warranties, whether express or implied, including, 
without limitation, any implied warranties of merchantability or
fitness for a particular purpose.

[Web Page](http://dvklopfenstein.github.io/PrincetonAlgorithms)
[github pages](https://help.github.com/pages)

Copyright (C) 2014-2019, DV Klopfenstein. All rights reserved.
