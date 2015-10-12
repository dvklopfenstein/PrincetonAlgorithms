# Implementations Summary

## ST implementations

|                   | worst-case cost          | average-case cost                  |             |         
| implementation    | search | insert | delete | search hit | insert    | delete    | ordered it? | key i/f
| --------------    | ------ | ------ | ------ | ---------- | ------    | --------- | ----------- | -------
| sequential search |   N    |   N    |   N    |    N/2     |   N       |    N/2    |     no      | equals()
| binary search     |  lg N  |   N    |   N    |   lg N     |  N/2      |    N/2    |    yes      | compareTo()
| BST               |   N    |   N    |   N    | 1.38 ln N  | 1.38 lg N |     ?     |    yes      | compareTo()
| red-black BST     | 2 lg N | 2 lg N | 2 lg N | 1.00 ln N  | 1.00 lg N | 1.00 lg N |    yes      | compareTo()
