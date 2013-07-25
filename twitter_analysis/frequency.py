"""
This program computes the term frequency histogram of the sample twitter data. 
The frequency of a term is calculated using following formula:
[No. of occurrences of the term in all tweets] / [No. of occurrences of all terms in all tweets]
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

import sys
import json

#-----------------------------------------------------------------------------#
def term_frequency(tweet_file):

    terms_count = {}

    for tweet in tweet_file:
        t = json.loads(tweet)

        if t.has_key('text'):              # it the tweet has 'text', then its valid tweet, otherwise its junk
            line = t['text'].split(' ')    # transform the tweet into a list of words
            for word in line:
                word = word.strip()
                if word not in terms_count:
                    terms_count[word] = 1
                else:
                    terms_count[word] += 1
    return terms_count

#-----------------------------------------------------------------------------#
def main():
    tweet_file = open(sys.argv[1])
    
    tweet_file.seek(0)   # move the file pointer back to top
    terms_count = term_frequency(tweet_file)
    tweet_file.close()

    k = len(terms_count) * 1.0
    for word in terms_count:
        print word, ":", terms_count[word]/k

#-----------------------------------------------------------------------------#    
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#