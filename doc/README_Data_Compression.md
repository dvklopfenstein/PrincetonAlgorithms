# Data Compression

## Code
  * **Introduction to Data Compression**
  * **Run-Length Coding**: RunLength.py
  * **Huffman Compression**: Huffman.py
  * **LZW Compression**: LZW.py(uses TST.py)

## Table of Contents for Practice Examples
  1. [Huffman trie](#Q1)    
  2. [LZW-encoded](#Q2)    
  3. [What is the result of compressing the following string of length 15 using LZW compression?](#Q3)    

## Examples 
### [Q1](#table-of-contents-for-examples)
**Huffman trie**    
```
Compute the Huffman trie for the following string of length 46?

    FPLIEELEIEIEDFDHDIFEDIEIEFDFIIEEDFEPFEIIFPPFPI

For reference, here are the frequencies of each of the characters in the string:

    char  freq
    ----------
       D     6
       E    12
       F     9
       H     1
       I    11
       L     2
       P     5


Using the encodings from the Huffman trie you computed, how many bits are needed
to encode the above string? Do not count the bits to represent the encoding table
or any bits used for padding and byte alignment.
```

### [Q2](#table-of-contents-for-examples)
**LZW-encoded**    
```
What is the result of expanding the following LZW-encoded sequence of 11 hexadecimal integers?

    43 42 43 81 83 41 84 42 82 41 80 

Assume the original encoding table consists of all 7-bit ASCII characters and uses 8-bit codewords.
Give your answer as a sequence of characters, with one space between each character.
```

### [Q3](#table-of-contents-for-examples)
**What is the result of compressing the following string of length 15 using LZW compression?**    
```
What is the result of compressing the following string of length 15 using LZW compression?

     A A C C B C C A A A C C C A C 

Assume the original encoding table consists of all 7-bit ASCII characters and uses 8-bit
codewords. Give your answer as a sequence of 11 hexadecimal integers, starting with 41
and ending with the stop codeword 80.
```

Copyright (C) 2002-2015 Robert Sedgewick and Kevin Wayne.  All rights reserved.    
Copyright (C) 2014-2015 DV Klopfenstein. All rights reserved. Python translation.
