A simple library for the [twitter streaming api](http://dev.twitter.com/pages/streaming_api)

Its as simple as:
<pre>
from twitter.stream import BaseStreamingHandler

class SimpleClass(BaseStreamingHandler):
    def process_tweet(self,tweet):
       print tweet['text']

streamer = SimpleClass('username', 'password')
streamer.track(['key', 'words'])
streamer.sample()
</pre>

you can also implement your own conversion of each tweet into a model of your choosing
by overriding <code>json_to_object</code> in your subclass.