import urllib2

class Request:

	@staticmethod
	def update():
		base = 'https://iitbbs.herokuapp.com/'

		news = urllib2.urlopen(base + 'news').read()
		notices = urllib2.urlopen(base + 'notices').read()
		events = urllib2.urlopen(base + 'events').read()

		nNews = open('json/new/news.json', 'w')
		nNews.write(news)
		nNews.close()

		nNotices = open('json/new/notices.json', 'w')
		nNotices.write(notices)
		nNotices.close()

		nEvents = open('json/new/events.json', 'w')
		nEvents.write(events)
		nEvents.close()