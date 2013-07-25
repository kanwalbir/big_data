"""
This program determines which state is happiest based on the sample twitter 
data. AFINN-111.txt contains a list of pre-computed sentiment scores. The 
user's location is determined based on the "place" object and is limited to 
only US.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

import sys
import json
from operator import itemgetter

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
def generate_tweet_score(line, scores):
    t_score = 0                    # initial tweet score to 0

    for word in line:
        t_score += find_word_score(word, scores) 

    return t_score  

#-----------------------------------------------------------------------------#
def score_states(tweet_file, scores):

    happy_states = {}

    for tweet in tweet_file:
        t = json.loads(tweet)
        text = t.get('text')     # verify if 'text' exists as key
        place = t.get('place')   # verify if 'place' exists as key
        #lang = t.get('lang')     # verify if 'lang' exists as key
        
        if text and place: # it the tweet has 'text', then its valid tweet, otherwise its junk
            #if lang == 'en' and t['place']['country_code'] == 'US':     # only check english language and US country tweets
            if t['place']['country_code'] == 'US':

                state = t['place']['full_name'].split(', ')[-1]   # seperate city from city, state
                if len(state) == 2:                  # only use two letter state abbrevation code
                    
                    line = t['text'].split(' ')    # transform the tweet into a list of words
                    t_score = generate_tweet_score(line, scores)
                    
                    if state not in happy_states:
                        happy_states[state] = t_score
                    else:
                        happy_states[state] += t_score

    return happy_states

#-----------------------------------------------------------------------------#
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    sent_file.seek(0)    # move the file pointer back to top
    scores = create_senti_scores(sent_file) 
    sent_file.close()
    
    tweet_file.seek(0)   # move the file pointer back to top
    happy_states = score_states(tweet_file, scores)
    tweet_file.close()

    happiest = max(happy_states.items(), key=itemgetter(1))[0]     # print the state with largest value
    print "\nThe happiest state as per the sample Twitter data collected is: " + happiest + "\n"

#-----------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------#
