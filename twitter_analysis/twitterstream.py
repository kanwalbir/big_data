"""
This program captures the Twitter live stream. Please look at the end of this 
file to switch between two ways to capture data. Also, please enter your secret 
Twitter tokens on line 19-23 before running this program.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#
import oauth2 as oauth
import urllib2 as urllib
import json

#-----------------------------------------------------------------------------#
"""
OAuth Authentication & Authorization. Enter the tokens from your specific 
Twitter Developer account below.
"""
access_token_key = "SECRET"
access_token_secret = "SECRET"

consumer_key = "SECRET"
consumer_secret = "SECRET"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

#-----------------------------------------------------------------------------#
"""
Construct, sign, and open a twitter request using the hard-coded credentials above.
"""
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

#-----------------------------------------------------------------------------#
"""
Fetches sample data from Twitter and outputs it to the screen. Let this run as 
long as you want and then do keyboard interrupt.
"""
def fetchsampledata():

  # Get a sample of twitter data
  url = "https://stream.twitter.com/1/statuses/sample.json"
  
  parameters = []
  response = twitterreq(url, "GET", parameters)
  for line in response:
    print line.strip()

#-----------------------------------------------------------------------------#
"""
Fetches specific data associated with a search term from Twitter and stores it 
in twitter_output.txt
"""
def fetchspecificdata():

  # Get recent tweets associated with the term microsoft
  search_term = "microsoft"

  parameters = []
  f = open("twitter_output.txt", "w")

  # Send the request to twitter 5 times to get large quantity of data
  for i in range(5):
    
    url = "https://api.twitter.com/1.1/search/tweets.json?q=" + search_term + "&count=100"
    response = twitterreq(url, "GET", parameters)

    j_response = json.load(response)
    f.write(str(j_response) + '\n')

  f.close()

#-----------------------------------------------------------------------------#
"""
Switch between fetchsampledata or fetchspecificdata as needed.
"""
if __name__ == '__main__':
  fetchsampledata()
  #fetchspecificdata()

#-----------------------------------------------------------------------------#