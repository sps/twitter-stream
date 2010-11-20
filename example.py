#!/usr/bin/env python
from twitter.stream import BaseStreamingHandler


class TestClass(BaseStreamingHandler):
	"""docstring for TestClass"""

	def process_tweet(self,tweet):
		"""docstring for process_tweet"""		
		try:
			print "%s -> %s\n" % (tweet['user']['screen_name'], tweet['text'])
		except KeyError:
		 	"""tweet was a delete or limit. handle as you see fit"""
			if tweet.has_key('delete'):
				print "DELETE %s\n" % (tweet['delete']['status'])
			else:
				print ','.join(tweet.keys())

if __name__ == '__main__':
	foo = TestClass("twitter_username", "password")
	foo.track(['bieber'])
	#foo.sample()
