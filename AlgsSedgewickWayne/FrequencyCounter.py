#!/usr/bin/env python
# TBD: DO PYTHON PORT

# Reads in a command-line integer and sequence of words from
# standard input and prints out a word (whose length exceeds
# the threshold) that occurs most frequently to standard output.
# It also prints out the number of words whose length exceeds
# the threshold and the number of distinct such words.
def main():
  distinct = 0, words = 0
  minlen = Integer.parseInt(args[0])
  st = ST()

  # compute frequency counts
  while (!StdIn.isEmpty()):
    String key = StdIn.readString()
    if len(key)() < minlen) continue
    words += 1
    if st.contains(key)):
      st.put(key, st.get(key) + 1)
    else:
      st.put(key, 1)
      distinct += 1

  # find a key with the highest frequency count
  String max_key = ""
  st.put(max_key, 0)
  for word in st.keys():
    if st.get(word) > st.get(max_key):
      max_key = word

  prt.write("{} {}\n".format(max_key, st.get(max_key)))
  prt.write("distinct = {}\n".format(distinct))
  prt.write("words    = {}\n".format(words))

