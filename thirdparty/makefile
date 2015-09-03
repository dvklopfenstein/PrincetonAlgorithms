
MAIN := HelloWorld

ALGS4SRC ?= .

JC := javac-algs4.bat
JVM := java-algs4.bat
CHK := checkstyle-algs4.bat
BUG := findbugs-algs4.bat
.PHONY: clean

SRCS = \
  StdArrayIO.java \
  StdDraw.java \
  StdIn.java \
  StdOut.java \
  StdRandom.java \
  StdStats.java \
  Stopwatch.java \
  Bag.java \
  BinarySearch.java \
  BouncingBalls.java \
  BST.java \
  Date.java \
  EvaluatePostfix.java \
  GrahamScan.java \
  Heap.java \
  HelloWorld.java \
  Insertion.java \
  Knuth.java \
  LinkedBag.java \
  LinkedQueue.java \
  LinkedStack.java \
  MaxPQ.java \
  Merge.java \
  MergeBU.java \
  MergeX.java \
  MinPQ.java \
  Point2D.java \
  Queue.java \
  Quick.java \
  Quick3way.java \
  QuickFindUF.java \
  QuickUnionUF.java \
  QuickX.java \
  ResizingArrayBag.java \
  ResizingArrayQueue.java \
  ResizingArrayStack.java \
  Selection.java \
  Shell.java \
  ST.java \
  Stack.java \
  ThreeSum.java \
  ThreeSumFast.java \
  UnorderedMaxPQ.java \
  WeightedQuickUnionUF.java

# If needed, clear any default definitions for these targets
.SUFFIXES: .java .class

# --------------------------------------------------------------
# Targets

run: $(MAIN).class
	$(JVM) $(MAIN)

# 'class' is the suffix of the target file
# 'java' is the suffix for the dependency file
# i.e. If MAIN.java source changes, re-compile MAIN.class
.java.class:
	$(JC) $(JFLAGS) $*.java

# Week 1 Programming Assignment 
wk1: Percolation.class PercolationStats.class
	$(JVM) $(JFLAGS) PercolationStats 10 2

wk1_zip:
	zip percolation.zip Percolation.java PercolationStats.java

wk2_zip:
	zip queues.zip Deque.java RandomizedQueue.java Subset.java

wk3_zip:
	zip collinear.zip Point.java Brute.java Fast.java

wk4_zip:
	zip 8puzzle.zip Board.java Solver.java

wk5_zip:
	zip kdtree.zip PointSET.java KdTree.java

Percolation.class: $(ALGS4SRC)/Percolation.java
	$(JC) -d . $<

PercolationStats.class: $(ALGS4SRC)/PercolationStats.java
	$(JC) -d . $<

clean:
	rm -f *.class

