import MapReduce
import sys
import itertools
from collections import defaultdict, Counter

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    id, code = record
    mr.emit_intermediate(code[:-10], None)

def reducer(code, _):
    mr.emit(code)

# Do not modify beow this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
