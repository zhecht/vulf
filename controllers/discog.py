from flask import *

discog = Blueprint('discog', __name__, template_folder='views')

@discog.route('/discography')
def discog_route():

	mitpeck = ["Beastly", "It Gets Funkier", "Rango", "Cars Too", "Prom", "Tomboy"]
	vollmilch = ["Outro", "A Walk to Remember", "Adrienne & Adrianne", "It Gets Funkier II", "Barbara", "Mean Girls"]
	tota = ["Welcome to Vulf Records", "Back Pocket", "Funky Duck", "Rango II", "Game Winner", "Walkies", "Christmas in L.A.", "Conscious Club", "Smile Meditation", "Guided Smile Meditation"]
	mfc = ["Wait for the Moment", "The Birdwatcher", "The Speedwalker", "My First Car", "Kulmilch 74 BPM", "It Gets Funkier III"]
	fugue = ["Fugue State", "1612", "First Place", "Sky Mall", "Christmas in L.A. (Instr)", "Newsbeat", "Christmas in L.A."]
	return render_template("discog.html", mitpeck=mitpeck, vollmilch=vollmilch, tota=tota, mfc=mfc, fugue=fugue)