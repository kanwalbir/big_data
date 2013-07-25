#-------------------------------------------------------#
#                            Twitter Analysis           #
#-------------------------------------------------------#

PROBLEM: Perform small-scale natural language processing (NLP) by accessing the Twitter API and performing sentiment analysis on the tweets.

After collecting a large sample of tweets, try to estimate public's perception/sentiment and analyze the relationship between location and mood based on sample data.
https://en.wikipedia.org/wiki/Sentiment_analysis#Sentiment_analysis_and_Web_2.0

SOLUTION: Please read the comments on the top of each python file for more details on what that particular program does.

IMPLEMENTATION: Step 1: python twitterstream.py > twitter_sample.txt
				Step 2:
						python tweet_sentiment.py AFINN-111.txt twitter_sample.txt
						python term_sentiment.py AFINN-111.txt twitter_sample.txt
						python frequency.py twitter_sample.txt
						python happiest_state.py AFINN-111.txt twitter_sample.txt
						python top_ten.py twitter_sample.txt
#-------------------------------------------------------#
