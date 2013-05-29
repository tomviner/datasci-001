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
    mr.emit_intermediate(tuple(sorted(record)), record)

def reducer(srtd, pairs):
    n = len(pairs)
    if n == 1:
        person, friend = pairs[0]
        mr.emit((person, friend))
        mr.emit((friend, person))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
