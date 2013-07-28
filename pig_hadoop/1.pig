/*

Count the number of tuples associated with each object in 'btc-2010-chunk-000'

http://km.aifb.kit.edu/projects/btc-2010/btc-2010-chunk-000.gz

*/

----------------------------------------------------------------

REGISTER myudfs.jar;

-- load the chunk-000 file into Pig
raw = LOAD 'btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- group the n-triples by object column
objects = group ntriples by (object) PARALLEL 50;

-- flatten the objects out and count the number of tuples associated with each object
count_by_object = foreach objects generate flatten($0), COUNT($1) as count PARALLEL 50;

-- store count_by_object into 's3n://fake_directory'
STORE count_by_object into 's3n://fake_directory/';

----------------------------------------------------------------

