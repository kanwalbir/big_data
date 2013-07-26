"""
Create an Inverted index. An inverted index is a dictionary where each word 
is associated with a list of the document identifiers in which that word appears. 

Mapper Input: [document_id, text]
              document_id: document identifier formatted as a string
              text: text of the document formatted as a string

Reducer Output: (word, document ID list)
                word: a string
                document ID list: list of Strings

python inverted_index.py data/books.json
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
    words = value.split()

    for w in words:
      mr.emit_intermediate(w, key)

#-----------------------------------------------------------------------------#
"""
Combines all intermediate values for a particular key and produces a set of 
merged output values
"""
def reducer(key, list_of_values):
    v = list(set(list_of_values))
    mr.emit((key, v))

#-----------------------------------------------------------------------------#
"""
Loads JSON file and executes the MapReduce query
"""
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

#-----------------------------------------------------------------------------#
