"""
Compute matrix multiplication: A x B where A and B are in a sparse matrix 
format, where each record is of the form i, j, value.

Mapper Input: Matrix row records formatted as lists [matrix, i, j, value]

Reducer Output: Matrix row records formatted as tuples (i, j, value)

python multiply.py data/matrix.json
"""

#-----------------------------------------------------------------------------#
import MapReduce
import sys
from operator import itemgetter

#-----------------------------------------------------------------------------#
"""
Creates a MapReduce object
"""
mr = MapReduce.MapReduce()

#-----------------------------------------------------------------------------#
"""
Processes input key-value pair and emits a set of intermediate key-value pairs
"""
def mapper(record):
    key = 'ab'
    value = record
    mr.emit_intermediate(key, value)

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    size = max(list_of_values, key=itemgetter(1))[1] + 1
    
    for i in range(size):
      for j in range(size):

        row_a, row_b = {}, {}

        for v in list_of_values:
          if v[0] == 'a' and v[1] == i:
            row_a[v[2]] = v[3]
          if v[0] == 'b' and v[2] == j:
            row_b[v[1]] = v[3]

        total = 0
        for k in range(size):
          if k in row_a and k in row_b:
            total += row_a[k] * row_b[k]

        mr.emit((i, j, total))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#