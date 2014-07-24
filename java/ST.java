// 9 - 1 Symbol Table API (21-30) at 4:23
//
// Basic symbol table API
//
// Associative array abstraction. Associate one value with each key.

public class ST<Key, Value>
              ST() // create a symbol table
         void put(Key key, Value val) // put key-value pair into the table
                                      // (remove key from table if value is null)
        Value get(Keykey) // value paired with key (null if key is absent)
         void delete(Key key) // remove key (and its value) from table
      boolean contains(Key key) // is there a value paired with key?
      boolean isEmpty() // is the table empty?
          int size() // number of key-value pairs in the table
Iterable<Key> keys() // all the keys in the table
