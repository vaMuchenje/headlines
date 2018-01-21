import feedparser

from flask import Flask, render_template

RSS_FEEDS = {
'herald':'http://www.herald.co.zw/feed/',
'newzimbabwe':'http://newzimbabwe.com/rss/rss.xml',
'mafaro':'http://www.mafaro.co.uk/feeds/posts/default',
'nehanda':'http://nehandaradio.com/feed/',
'independent':'https://www.theindependent.co.zw/feed/',
'newsday':'https://www.newsday.co.zw/feed/'}

app = Flask(__name__)


@app.route('/')
@app.route('/<publication>')
def get_news(publication="herald"):
	feed = feedparser.parse(RSS_FEEDS[publication])
	articles = feed['entries']
	return render_template("home.html", articles=articles)

if __name__ == '__main__':
	app.run(port=5000, debug=True)