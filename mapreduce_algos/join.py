"""
Implement a relational join as a MapReduce query:
SELECT * FROM Orders, LineItem WHERE Order.order_id = LineItem.order_id

Mapper Input: lists of Strings

Reducer Output: a joined record

python join.py data/records.json
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
    key = record[1]
    mr.emit_intermediate(key, record)

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    
    for v in list_of_values:
      if v[0] == 'order':
        a = v
    
    for v in list_of_values:
      if v[0] == 'line_item':
        mr.emit((a+v))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#
