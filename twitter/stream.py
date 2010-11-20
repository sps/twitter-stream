import json
import urllib2
import base64

class BaseStreamingHandler(object):
	"""docstring for BaseStreamingHandler"""
	
	def __init__(self, username="", password=""):
		super(BaseStreamingHandler, self).__init__()
		self.username = username;
		self.password = password;

	def process_tweet(self,tweet):
		"""process_tweet stub. implement this in your subclass"""
		raise RuntimeError('you must implement process_tweet')

	def json_to_object(self,json_string):
		"""convert a tweet from a json string to a dict"""
		return json.loads(json_string)

	def track(self,keywords=[]):
		"""stream tweets that match a list of keywords"""
		self.__stream(self.__make_request("%s?track=%s" % ('http://stream.twitter.com/1/statuses/filter.json', urllib2.quote(','.join(keywords)))))

	def sample(self):
		"""Streams a random sample of all public statuses."""
		self.__stream(self.__make_request('http://stream.twitter.com/1/statuses/sample.json'))

	def __stream(self,request):
		"""docstring for __stream"""
		stream = urllib2.urlopen(request)
		cur_data = ""
		try:
			while 1:
			    cur_data += stream.read(1024) # this could probably be optimized
			    try:
			        pos = cur_data.index("\n")
			        json_str = cur_data[:pos]
			        cur_data = cur_data[pos+1:]
			        self.process_tweet(self.json_to_object(json_str))
			    except ValueError:
			        pass
		except KeyboardInterrupt:
			pass
		finally:
			stream.close()

	def __make_request(self,url):
		"""helper method to add auth header to requests"""
		request = urllib2.Request(url)
		## add authentication header:
		request.add_header("Authorization", "Basic %s" % base64.encodestring('%s:%s' % (self.username, self.password))[:-1])
		return request
		
