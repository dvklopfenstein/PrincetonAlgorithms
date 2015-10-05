
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class test_RandomizedQueue {

    public static void main(String[] argv) {
        RandomizedQueue<String> rq = new RandomizedQueue<String>();
        rq.enqueue("A");  
        rq.enqueue("B");  
        for (String outerItem : rq) {  
            for(String innerItem :rq) {  
                System.out.println(outerItem + innerItem);  
            }  
        }
    }

}

// Subset client. Write a client program Subset.java that takes
// a command-line integer k; reads in a sequence of N strings
// from standard input using StdIn.readString(); and prints out
// exactly k of them, uniformly at random. Each item from the
// sequence can be printed out at most once. You may assume
// that 0 ≤ k ≤ N, where N is the number of string on standard
// input.
// 
// % echo A B C D E F G H I | java Subset 3       % echo AA BB BB BB BB BB CC CC | java Subset 8
// C                                              BB
// G                                              AA
// A                                              BB
//                                                CC
// % echo A B C D E F G H I | java Subset 3       BB
// E                                              BB
// F                                              CC
// G                                              BB
// 
// The running time of Subset must be linear in the size of the
// input. You may use only a constant amount of memory plus
// either one RandomizedQueue or RandomizedQueue object of maximum size
// at most N, where N is the number of strings on standard
// input. (For an extra challenge, use only one RandomizedQueue or
// RandomizedQueue object of maximum size at most k.) 

