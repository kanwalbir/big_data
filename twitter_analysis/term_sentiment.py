"""
This program derives the sentiment of new terms that do not appear in the file 
AFINN-111.txt. The term-sentiment is based on the sentiment score of the tweet  
that contains that particular new term.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

import sys
import json

#-----------------------------------------------------------------------------#
def create_senti_scores(sent_file):
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
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
def create_word_score(line, tweet_score, not_found, scores):
    
    for word in line:
        if word not in scores:
            if word not in not_found:
                not_found[word] = (tweet_score * 1.0, 1)  # save the tweet_score and frequency of the word
            else:
                f = not_found[word][1]
                s = not_found[word][0]
                new_f = f + 1                            # increase word frequency by 1
                new_s = ((f * s) + tweet_score)/new_f    # incrase word score by normalization
                not_found[word] = (new_s , new_f)
    
    return not_found

#-----------------------------------------------------------------------------#
def print_word_score(line, not_found, scores):
    for word in line:
        
        if word in scores:                   # if word score is pre-generated, display that score
            print word, scores[word]
        
        elif word in not_found:              # if word score is based on tweet score, display that score
            print word, "%.2f" % not_found[word][0]
        
        else:                                # all else fails, print 0
            print word, 0.0

#-----------------------------------------------------------------------------#
def generate_tweet_score(tweet_file, scores):

    not_found = {}

    for tweet in tweet_file:
        t = json.loads(tweet)

        if t.has_key('text'):              # it the tweet has 'text', then its valid tweet, otherwise its junk
            t_score = 0                    # initial tweet score to 0
            line = t['text'].split(' ')    # transform the tweet into a list of words
            for word in line:
                t_score += find_word_score(word, scores)
            
            not_found = create_word_score(line, t_score, not_found, scores)   # generate word score, if word score not provided
            print_word_score(line, not_found, scores)                         # print word scores

        else:
            print 0

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