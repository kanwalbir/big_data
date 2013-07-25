"""
This program derives the sentiment of each tweet based on the sentiment scores 
of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of 
the sentiment scores for each term in the tweet. AFINN-111.txt contains a list 
of pre-computed sentiment scores. Any word found in a tweet, but not in 
AFINN-111.txt is given a sentiment score of 0.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

import sys
import json

#-----------------------------------------------------------------------------#
def create_senti_scores(sent_file):
    scores = {}

    for line in sent_file:
        term, score  = line.split("\t")
        scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary
    #print len(scores)
    return scores

#-----------------------------------------------------------------------------#
def find_word_score(word, scores):
    if word in scores:        # if word is in scores dictionary, return the score, otherwise 0
        return scores[word]
    return 0

#-----------------------------------------------------------------------------#
def generate_tweet_score(tweet_file, scores):

    for tweet in tweet_file:
        t = json.loads(tweet)

        if t.has_key('text'):              # it the tweet has 'text', then its valid tweet, otherwise its junk
            t_score = 0                    # initial tweet score to 0
            line = t['text'].split(' ')    # transform the tweet into a list of words
            for word in line:
                t_score += find_word_score(word, scores)
            print line, " - Score:", t_score
        
        else:
            print line, " - Score:", 0

#-----------------------------------------------------------------------------#
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sent_file.seek(0)    # move the file pointer back to top
    scores = create_senti_scores(sent_file) 
    sent_file.close()
    
    tweet_file.seek(0)   # move the file pointer back to top
    generate_tweet_score(tweet_file, scores)
    tweet_file.close()

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#
