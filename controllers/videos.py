from flask import *

videos = Blueprint('videos', __name__, template_folder='views')

@videos.route('/videos')
def videos_route():



	album = ["Mit Peck", "Vollmilch", "My First Car", "Fugue State", "Thrill of the Arts"]
	links = ["https://www.youtube.com/watch?v=hvcjhES2-Hs", "https://www.youtube.com/watch?v=3WYiC-oXVBc" ,"https://www.youtube.com/watch?v=uqbsS8cRNoU" ,"https://www.youtube.com/watch?v=6Tsdb5Wp4fg","https://www.youtube.com/watch?v=wJIFJ-L-Lw8"]

	albums = []
	i = 0
	for a in album:
		albums.append({'album': a, 'link': links[i]})
		i += 1


	cover = ["Cripple Creek","It Gets Funkier & I Wish", "Good Times & We Are Family", "Speedwalker & Oh What a Night", "Got to Be Real", "I Want You Back", "Dancing in the Moonlight"]
	links = ["https://www.youtube.com/watch?v=GeCMbfoQQPw","https://www.youtube.com/watch?v=s9g7MFAyqws", "https://www.youtube.com/watch?v=Qej_-gBCGX4", "https://www.youtube.com/watch?v=AQk701qQbMQ", "https://www.youtube.com/watch?v=Bm7DwRrKxQM", "https://www.youtube.com/watch?v=3rgX3zCEdp4", "https://www.youtube.com/watch?v=9rWdzSom4gE"]

	covers = []
	i = 0
	for c in cover:
		covers.append({'cover': c, 'link': links[i]})
		i += 1

	ant = []

	antwaun = ["Wait for the Moment (Blind Pig, AA)", "Wait for the Moment (Sonic Lunch, Ann Arbor)", "1612 (Colbert)", "1612 (Blind Pig)", "1612 (Brooklyn Bowl)"]
	links = ["https://www.youtube.com/watch?v=RCJ3ErG8Gro", "https://www.youtube.com/watch?v=AmubT7YiOfA", "https://www.youtube.com/watch?v=ceuIz7dMA8Q", "https://www.youtube.com/watch?v=u0iBVgZ3cmk", "https://www.youtube.com/watch?v=y89N7_PDoC8"]

	i = 0
	for a in antwaun:
		ant.append({'song': a, 'link': links[i]})
		i += 1

	joey = []

	dosik = ["Game Winner (w/ Theo)", "Outro & Speedwalker"]
	links = ["https://www.youtube.com/watch?v=NWZJ2TXUC-U", "https://www.youtube.com/watch?v=NWZJ2TXUC-U"]

	i = 0
	for d in dosik:
		joey.append({'song': d, 'link': links[i]})
		i += 1

	blake = []
	mills = ["Rango II (Teragram Ballroom", "Que Sera Sera (w/ dosik)"]
	links = ["https://www.youtube.com/watch?v=4wbYPDtXdf4", "https://www.youtube.com/watch?v=gTz6y9rGktA"]
	i = 0
	for m in mills:
		blake.append({'song': m, 'link': links[i]})
		i += 1

	return render_template("videos.html", albums=albums, covers=covers, ant=ant, joey=joey, blake=blake)