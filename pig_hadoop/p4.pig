/*
Create histogram data showing the distribution of counts per subject and generate scatter-plot on entire dataset (all chunk files). The histogram consists of:

X-axis: Counts associated with the subjects
Y-axis: Total number of subjects associated with each particular count

http://km.aifb.kit.edu/projects/btc-2010/000-CONTENTS
OUTPUT FILE: output_4.txt
*/

----------------------------------------------------------------

REGISTER myudfs.jar;

-- load all the chunk files into Pig
raw = LOAD 'btc-2010-chunk-*' USING TextLoader as (line:chararray);

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

-- group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the subjects out and count the number of tuples associated with each subject
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

x = foreach count_by_subject generate ($1);
y = group x by ($0);
z = foreach y generate flatten($0), COUNT($1);

-- store z into 's3n://fake_directory'
STORE z into 's3n://fake_directory/';

----------------------------------------------------------------
