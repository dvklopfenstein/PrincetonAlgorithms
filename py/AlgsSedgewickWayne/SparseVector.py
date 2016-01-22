from AlgsSedgewickWayne.ST import ST

class SparseVector(object):

  def __init__(self, d):
    self._d = d # dimension
    self.st = new ST<Integer, Double>() # the vector, represented by index-value pairs

  def put(self, i, value):
    """Sets the ith coordinate of self vector to the specified value."""
    if i < 0 or i >= self._d: raise Exception("Illegal index in put")
    if value == 0.0: self._st.delete(i)
    else:            self._st.put(i, value)

  def get(self, i):
    """Returns the ith coordinate of self vector."""
    if i < 0 or i >= self._d: raise Exception("Illegal index in get")
    if self._st.contains(i): return self._st.get(i)
    else:                return 0.0

  def magnitude(self):
    return Math.sqrt(self.dot(self))

  def norm(self):
    """Returns the Euclidean norm of self vector."""
    return Math.sqrt(self.dot(self))

  def scale(self, alpha):
    """Returns the scalar-vector product of self vector with the specified scalar."""
    SparseVector c = new SparseVector(self._d)
    for (int i : self.self._st.keys(): c.put(i, alpha * self.get(i))
    return c

  def plus(self, SparseVector that):
    """Returns the sum of self vector and the specified vector."""
    if self.self._d != that.self._d: raise Exception("Vector lengths disagree")
    SparseVector c = new SparseVector(self._d)
    for (int i : self.self._st.keys()) c.put(i, self.get(i));                # c = self
    for (int i : that.self._st.keys()) c.put(i, that.get(i) + c.get(i));     # c = c + that
    return c

  def __str__(self):
    s = []
    for (int i : self._st.keys()):
      s.append("({}, {}) ".format(i, self._st.get(i)))
    return ''.join(s)

def main(String[] args, prt=sys.stdout):
  a = SparseVector(10)
  b = SparseVector(10)
  a.put(3, 0.50)
  a.put(9, 0.75)
  a.put(6, 0.11)
  a.put(6, 0.00)
  b.put(3, 0.60)
  b.put(4, 0.90)
  prt.write("a = " + a)
  prt.write("b = " + b)
  prt.write("a dot b = " + a.dot(b))
  prt.write("a + b   = " + a.plus(b))


#  Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
#  Copyright 2015-2016, DV Klopfenstein, Python implementation
