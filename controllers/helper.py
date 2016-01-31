from flask import *
import urllib2
import json
import constants
from datetime import datetime
from dateutil import tz #pip install python-dateutil
import oauth2 as oauth

fb_consumer = oauth.Consumer(key=constants.FB_APP_ID, secret=constants.FB_SECRET)
fb_client = oauth.Client(fb_consumer)

#twitter oauth
t_consumer = oauth.Consumer(key=constants.TWITTER_CONSUMER_KEY, secret=constants.TWITTER_CONSUMER_SECRET)
access_token = oauth.Token(key=constants.TWITTER_ACCESS_KEY, secret=constants.TWITTER_ACCESS_SECRET)
t_client = oauth.Client(t_consumer, access_token)

def get_fb_page_data(page_id, params):

	#vulf id: 285479221497876

	#endpoint = "https://graph.facebook.com/v2.5/"
	#graph_url = endpoint+page_id+ "?"+params
	#resp, content = fb_client.request(graph_url)
	#content_dict = json.loads(content)

	content_dict = json.loads(open("static/json/fb.json").read(), strict=False)
	return content_dict

def get_fb_posts(allData, name):
	posts = []
	for data in allData:
		try:
			pic = data['picture']
		except:
			pic = ""
		try:
			message = data['message']
		except:
			message = ""
		try:
			story = data['story']
		except:
			story = ""
		try:
			link = data['link']
		except:
			link = ""

		#2015-11-03T15:00:00+0000
		created_time = data['created_time']
		dt = datetime.strptime(created_time, "%Y-%m-%dT%H:%M:%S+0000")
		to_zone = tz.tzlocal()
		from_zone = tz.tzutc()

		utc = dt.replace(tzinfo=from_zone)
		time = utc.astimezone(to_zone)


		if message == "":
			message = story
		postId = data['id']
		posts.append({'picture': pic, 'message': message, 'created': time.strftime("%-I:%M %p %-m/%-d/%y"), 'id': postId, 'name': name, 'link': link.split(".com")[0][8:] + ".com", 'href': link})

	return posts


#twitter
def query_twitter(query):
	
	encoded_query = urllib2.quote(query)
	endpoint = "https://api.twitter.com/1.1/search/tweets.json?count=5&q=" + encoded_query
	response, data = t_client.request(endpoint)
	
	tweets = []
	tweets.append(json.loads(data))
	
	tweetss = tweets[0]['statuses']
	
	text = []
	tweet_time = []
	tweet_author = []
	tweet_name = []
	ptweet = []
	for tweet in tweetss:

		text = (tweet['text'])
		tweet_time = (tweet['created_at'])
		tweet_author = (tweet['user']['screen_name'])
		tweet_name = (tweet['user']['name'])
		tweet_entities = tweet['entities']
		tweet_hashtags = tweet_entities['hashtags']
		#tweet_mentions = tweet_entities['user_mentions']
		#tweet_mentions_name = tweet_mentions[0]['name']
		ptweet.append({'text': text, 'time': tweet_time, 'author': tweet_author, 'name': tweet_name})
	return ptweet


def query_user_twitter(artistid):
	#vulfpeck id: 661069712013590528

	vid = '525993877'
	tweets = []

	if vid == artistid:
		tweets.append(json.loads(open("static/json/twitter.json").read(), strict=False))
	else:
		endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?count=25&include_rts=false&exclude_replies=true&user_id=" +artistid
		response, data = t_client.request(endpoint)
		tweets.append(json.loads(data))
	
	
	tweetss = tweets[0]
	ptweet = []
	ind = 0
	for tweet in tweetss:

		
		text = (tweet['text']).replace("\n", "")
		isStatus = tweet['is_quote_status']
		tweet_time = (tweet['created_at'])
		tweet_author = (tweet['user']['screen_name'])
		tweet_name = (tweet['user']['name'])
		tweet_entities = tweet['entities']
		tweet_urls = tweet_entities['urls']

		tweet_url = ""
		start_index = 0
		end_index = 0
		tweet_url = ""
		display_url = ""

		if len(tweet_urls) > 0:
			url = tweet_urls[0]
			tweet_url = url['url']
			display_url = url['display_url']
			start_index = url['indices'][0]
			end_index = url['indices'][1]

		tweet_hashtags = tweet_entities['hashtags']
		tweet_mentions = tweet_entities['user_mentions']

		#Fri Mar 16 03:30:10 +0000 2012
		dt = datetime.strptime(tweet_time, "%a %b %d %H:%M:%S +0000 %Y")
		to_zone = tz.tzlocal()
		from_zone = tz.tzutc()
		utc = dt.replace(tzinfo=from_zone)
		time = utc.astimezone(to_zone)

		date = time.strftime("%-I:%M %p %-m/%-d/%y")

		if len(tweet_mentions) > 0:
			tweet_mentions_name = tweet_mentions[0]['name']
		ptweet.append({'ind': ind, 'text': text, 'time': date, 'author': tweet_author, 'name': tweet_name, 'url': tweet_url, 'display_url': display_url, 'start': start_index, 'end': end_index})
		ind += 1

	return ptweet

def get_user_id(artist):
	encoded_query = urllib2.quote(artist)
	endpoint = "https://api.twitter.com/1.1/users/search.json?count=2&q=" +encoded_query
	response, data = t_client.request(endpoint)

	tweets = []
	tweets.append(json.loads(data))
	
	return tweets[0][0]['id_str']

def get_events(vid):
	url = "http://api.songkick.com/api/3.0/artists/6634379/calendar.json?apikey=" + constants.SONGKICK_KEY
	#req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	#con = urllib2.urlopen(req)

	con = open("static/json/songkick.json")
	results = json.loads(con.read(), strict=False)['resultsPage']['results']['event']

	events = []
	i = 0

	for event in results:
		displayName = event['displayName']
		start_date = event['start']['datetime']

		shortdate = 0
		if start_date == None:
			start_date = event['start']['date']
			dt = datetime.strptime(start_date, "%Y-%m-%d")
			shortdate = 1
		else:
			dt = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S-0600")
		performers = event['performance']

		artists = []
		count = 0
		#artists = ''
		for p in performers:
			

			#artists += p['displayName'] + ", "
			artists.append(p['displayName'])
			count += 1

			if count == 5:
				if "Vulfpeck" not in artists:
					artists.append("Vulfpeck")
				break


		
		venueName = event['venue']['displayName']
		locName = event['venue']['metroArea']['displayName']
		locState = event['venue']['metroArea']['state']['displayName']


		
		to_zone = tz.tzlocal()
		from_zone = tz.tzutc()

		utc = dt.replace(tzinfo=from_zone)
		time = utc.astimezone(to_zone)

		date = ''
		if shortdate == 1:
			date = time.strftime("%-m/%-d/%y")
		else:
			date = time.strftime("%-I:%M %p %-m/%-d/%y")
		events.append({'name': displayName, 'start': date, 'artists': artists, 'venue': venueName, 'location': locName + ", " + locState, 'index': i, 'total_artists': len(artists)})

		i += 1

	return events




