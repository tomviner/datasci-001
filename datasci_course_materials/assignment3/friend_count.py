import MapReduce
import sys
import itertools
from collections import defaultdict

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    user = record[0]
    friend = record[1]
    mr.emit_intermediate(user, friend)

def reducer(user, friends):
    mr.emit((user, len(friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
