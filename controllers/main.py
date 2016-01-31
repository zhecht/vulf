from flask import *
from helper import *
import constants

main = Blueprint('main', __name__, template_folder='views')



@main.route('/')
def main_route():


	who = request.args.get('user')
	user = ''
	fb_id = '285479221497876'
	t_id = '525993877'
	if who == None or who == '':
		who = "Vulpeck"
		user = "Vulfpeck"
		t_id = '525993877'
	elif who == "woody":
		t_id = '231316936'
		user = "Woody"
	elif who == "theo":
		t_id = '257224067'
		user = "Theo"
	elif who == "antwaun":
		t_id = ''
	elif who == "joe":
		t_id = '434690062'
		user = "Dart"
	elif who == 'jack':
		t_id = '45193013'
		user = "Jack"


	#fb
	token = constants.FB_ACCESS
	name = "Vulfpeck"

	page_query = fb_id + "/posts"
	params = "fields=picture,message,story,created_time,link,id&access_token="+token
	page_data = get_fb_page_data(page_query, params)
	allData = page_data['data']
	posts = get_fb_posts(allData, name)

	#twitter
	#ptweet = query_twitter("Theo Katzman")
	ptweet = query_user_twitter(t_id)
	
	#events
	events = get_events("6634379")

	#events = []
	#ptweet = []
	#posts = []

	member = ["Theo", "Woody", "Ace of Bass", "Jack", "Vulfpeck"]
	links = ["theo", "woody", "joe", "jack", "Vulfpeck"]
	members = []
	i = 0
	for m in member:
		if links[i] != who:
			members.append({'name': m, 'link': links[i]})
		i += 1

	return render_template("main.html", tweets=ptweet, posts=posts, events=events, user=user, members=members)
