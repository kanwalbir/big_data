#-------------------------------------------------------#
#         			Billion Triples				        #
#-------------------------------------------------------#

PROBLEM: Billion triple dataset is an RDF dataset that contains about a billion triples from the Semantic Web, obtained by a crawler that extracted all RDF triples from the Web. RDF data is represented in triples of the form:

subject  predicate  object  [context](optional, not part of the triple)

The purpose of this project is to compute the out-degree (number of edges coming out of the node) of each node in the dataset. Initially, a small dataset (btc-2010-chunk-000) is used to test the accuracy of the problem, before running it on the entire dataset. Please read the comments on the top of each pig file for more details.

DATA SOURCE: http://km.aifb.kit.edu/projects/btc-2010/
			 http://km.aifb.kit.edu/projects/btc-2010/000-CONTENTS

DATA SIZE: 634GB - 317 files, each 2GB in size

IMPLEMENTATION: Performed on Amazon Web Services (AWS) using Elastic MapReduce job flows
				http://console.aws.amazon.com/elasticmapreduce/home

#-------------------------------------------------------#



