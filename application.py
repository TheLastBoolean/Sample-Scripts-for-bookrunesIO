from flask import Flask, render_template, url_for
application = Flask(__name__)

@application.route("/")
@application.route("/home")
def home():
	return render_template('home.html')

@application.route("/analytics")
def analytics():
	return graph


if __name__ == "__main__":
	application.debug = True
	application.run()