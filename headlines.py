import feedparser

from flask import Flask, render_template

from flask import request

RSS_FEEDS = {
'herald':'http://www.herald.co.zw/feed/',
'newzimbabwe':'http://newzimbabwe.com/rss/rss.xml',
'mafaro':'http://www.mafaro.co.uk/feeds/posts/default',
'nehanda':'http://nehandaradio.com/feed/',
'independent':'https://www.theindependent.co.zw/feed/',
'newsday':'https://www.newsday.co.zw/feed/'}

app = Flask(__name__)


@app.route('/')
def get_news():
	query = request.args.get("publication")
	if not query or query.lower() not in RSS_FEEDS:
		publication = 'herald'
	else:
		publication = query.lower()
	feed = feedparser.parse(RSS_FEEDS[publication])
	return render_template("home.html", articles = feed['entries'])

if __name__ == '__main__':
	app.run(port=5000, debug=True)