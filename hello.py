from flask import Flask, request, render_template, redirect, url_for, flash, session
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
			session['username'] = request.form.get('username')
			return redirect(url_for('welcome'))
		else:	
			error = "Incorrect username and password"
	return render_template('login.html', error=error)

@app.route("/logout")
def logout():
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/')
def welcome():
	if 'username' in session:
		return render_template('welcome.html', username=session['username'])
	else:
		return redirect(url_for('login'))

def valid_login(username,password):
	if username == password:
		return True
	else:
		return False

if __name__ == "__main__":
	app.secret_key = '\x0b\x8b\xac\x8fa\xa0\xa4\x81\xc7G\x13\xad\xee\x9aW\xa7$\x02\x96\x88\xf5Q\xa2\x17'
	app.debug = True
	app.run()

