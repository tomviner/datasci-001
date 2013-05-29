import MapReduce
import sys
import itertools
from operator import mul
from collections import defaultdict, Counter

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
product = lambda ns: reduce(mul, ns)

SIZE = 5

def mapper(record):
    matrix, i, j, value = record
    x, y = None, None
    if matrix == 'a':
        x = i
    else:
        assert matrix == 'b'
        y = j
    for n in range(SIZE):
        target = (
            n if x is None else x,
            n if y is None else y,
        )
        mr.emit_intermediate(target, (matrix, i, j, value))

def reducer(coords, values):
    x, y = coords
    m = {
        'a': defaultdict(int),
        'b': defaultdict(int),
    }
    for matrix, i, j, value in values:
        m[matrix][(i, j)] = value
    prods = [m['a'][(x, n)] * m['b'][(n, y)] for n in range(SIZE)]
    val = sum(prods)
    mr.emit((x, y, val))

# Do not modify beow this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
