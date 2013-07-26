"""
Remove the last 10 characters from each string of nucleotides, then remove any 
duplicates generated. 

Mapper Input: [sequence id, nucleotides]
              sequence id: Unique identifier formatted as a string
              nucleotides: Sequence of nucleotides formatted as a string

Reducer Output: unique trimmed nucleotide strings

python unique_trims.py data/dna.json
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
    key = 1
    value = record[1][:-10]
    mr.emit_intermediate(key, value)

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    list_of_values = list(set(list_of_values))
    for v in list_of_values:
      mr.emit((v))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#