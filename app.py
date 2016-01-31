from flask import Flask, render_template
import controllers
import os

app = Flask(__name__, template_folder='views')

app.register_blueprint(controllers.main)
app.register_blueprint(controllers.discog)
app.register_blueprint(controllers.videos)

app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)