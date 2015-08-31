from flask import Flask, request, render_template, redirect, url_for, flash
import datetime

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
	now = datetime.datetime.now()
	error = None
	if request.method == "POST":
		if valid_login(
			request.form.get('username'),
			request.form.get('password')
		):
			flash("Successfully logged in!")
			flash("Login time: %s" % now)
			return redirect(url_for('welcome', username=request.form.get('username')))
		else:	
			error = "Incorrect username and password"
	return render_template('login.html', error=error)

@app.route('/welcome/<username>')
def welcome(username):
	return render_template('welcome.html', username=username)

def valid_login(username,password):
	if username == password:
		return True
	else:
		return False

if __name__ == "__main__":
	app.secret_key = 'SuperSecretKey'
	app.debug = True
	app.run()

