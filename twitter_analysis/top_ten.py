"""
This program computes the ten most frequently occurring hash tags as per the 
sample collected data.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

import sys
import json
from operator import itemgetter

#-----------------------------------------------------------------------------#
def hashtag_count(tweet_file):

    hash_count = {}

    for tweet in tweet_file:
        t = json.loads(tweet)
        if t.has_key('entities'):    # if the tweet has 'entities', then its valid tweet, otherwise its junk
            
            for i in range(len(t['entities']['hashtags'])):     # a tweet may have many hashtags, so iterate over the list
                hashtag = t['entities']['hashtags'][i]['text']  # hashtag info is in the 'text' field of 'hashtags'

                if hashtag not in hash_count:
                    hash_count[hashtag] = 1.0
                else:
                    hash_count[hashtag] += 1
    
    return hash_count

#-----------------------------------------------------------------------------#
def main():
    tweet_file = open(sys.argv[1])
    
    tweet_file.seek(0)   # move the file pointer back to top
    hash_count = hashtag_count(tweet_file)
    tweet_file.close()

    all_hashtags = sorted(hash_count.items(), key=itemgetter(1), reverse=True)
    top_ten = all_hashtags[0:10]             # extract top 10 hashtags

    print "\nThe top 10 hash tags are:\n"
    for hashtag in top_ten:
        print hashtag[0], ":", hashtag[1]
    print "\n"

#-----------------------------------------------------------------------------#   
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#