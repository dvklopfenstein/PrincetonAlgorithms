#!/usr/bin/env python3
#*****************************************************************************
 #  H-tree.
 #    * O(1)  --  Used in Python's os.path.exists with an ext4 filesystem
 #    * https://stackoverflow.com/questions/6176547/python-complexity-of-os-path-exists-with-a-ext4-filesystem
 #    * Unlike standard B-tree, HTree has:
 #      * Constant depth
 #      * Uses hash-map per node, thus its lookup complexity is O(1{
 #    * http://ext2.sourceforge.net/2005-ols/paper-html/node3.html
 #    * https://en.wikipedia.org/wiki/HTree
 #    * improved the scalability of Linux ext2 based filesystems from a practical limit of a few thousand files,
 #      into the range of tens of millions of files per directory
 #    * 2000: Developed by Daniel Phillips
 #    * 2001: Implemented for the ext2 filesystem
 #    * 2002: Ported to ext3 by Christopher Li and Andrew Morton
 #
 #  Limitations
 #  -----------
 #
 #*****************************************************************************/

