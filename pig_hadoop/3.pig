/*

btc-2010-chunk-000
http://km.aifb.kit.edu/projects/btc-2010/btc-2010-chunk-000.gz

*/


----------------------------------------------------------------

REGISTER myudfs.jar;

-- load the chunk-000 file into Pig
raw = LOAD 'btc-2010-chunk-000' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

rdf_match = FILTER ntriples by subject matches '.*rdfabout\\.com.*';
rdf_match2 = foreach rdf_match generate subject as subject2, predicate as predicate2, object as object2;
rdf_join = join rdf_match by $2, rdf_match2 by $0;
distinct_rdf = distinct rdf_join;

-- store distinct_rdf into 's3n://fake_directory'
STORE distinct_rdf into 's3n://fake_directory/';

----------------------------------------------------------------
