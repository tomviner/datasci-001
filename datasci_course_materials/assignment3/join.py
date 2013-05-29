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
    table = record[0]
    order_id = record[1]
    fields = record
    mr.emit_intermediate(order_id, fields)

def reducer(order_id, list_of_fields):
    d = defaultdict(list)
    for fields in list_of_fields:
        table = fields[0]
        d[table].append(fields)
    for start, end in itertools.product(d['order'], d['line_item']):
        mr.emit(start + end)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
