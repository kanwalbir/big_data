"""
Count the number of friends each person has in a social network dataset 
consisting of key-value pairs where each key is a person and each value 
is a friend of that person.

Mapper Input: [person A, person B]

Reducer Output: (person, friend count)

python friend_count.py data/friends.json
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

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    total = len(list_of_values)
    mr.emit((key, total))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#