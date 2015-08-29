from flask import Flask, request
app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "POST":
		return "username is %s" % request.values["username"]
	else:
		return '<form method="post" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button>'

if __name__ == "__main__":
	app.debug = True
	app.run()

