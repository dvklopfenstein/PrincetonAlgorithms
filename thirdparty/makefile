

# Week 1 Programming Assignment 
# https://class.coursera.org/algs4partI-005/assignment/view?assignment_id=1
wk1: Percolation.class PercolationStats.class
	java -classpath . PercolationStats 10 2
	
wk1_zip:
	zip percolation.zip Percolation.java PercolationStats.java

Percolation.class: Percolation.java
	javac Percolation.java

PercolationStats.class: PercolationStats.java
	javac PercolationStats.java

clean:
	rm -f *.class
