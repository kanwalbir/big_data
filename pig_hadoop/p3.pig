/*
Perform a join on a subset of btc-2010-chunk-000 where subject matches 'rdfabout.com'

http://km.aifb.kit.edu/projects/btc-2010/btc-2010-chunk-000.gz
OUTPUT FILE: output_3.txt
*/

----------------------------------------------------------------

REGISTER myudfs.jar;

-- load the chunk-000 file into Pig
raw = LOAD 'btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- filter on subject matches '.*rdfabout\\.com.*' and make a copy
rdf_match = FILTER ntriples by subject matches '.*rdfabout\\.com.*';
rdf_match2 = foreach rdf_match generate subject as subject2, predicate as predicate2, object as object2;

-- perform join on two copies
rdf_join = JOIN rdf_match by $2, rdf_match2 by $0;
distinct_rdf = DISTINCT rdf_join;

-- store distinct_rdf into 's3n://fake_directory'
STORE distinct_rdf into 's3n://fake_directory/';

----------------------------------------------------------------
