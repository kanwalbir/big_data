"""
Check if the friend relationship is symmetric and generate a list of all 
non-symmetric friend relationships.

Mapper Input: [personA, personB]

Reducer Output: (person, friend) and (friend, person) for each asymmetric friendship

python asymmetric_friendships.py data/friends.json
"""

#-----------------------------------------------------------------------------#
import MapReduce
import sys

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
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value, key)

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    for v in list_of_values:
      if list_of_values.count(v) == 1:
        mr.emit((key, v))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#