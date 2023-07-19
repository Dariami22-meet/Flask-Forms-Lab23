from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

username = "Daria"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi","Alma", "Shiri"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		username1=request.form['username']
		password1= request.form['password']
		
		if username==username1 and password==password1:
					
					return redirect(url_for('home'))
	return render_template('login.html')



@app.route('/home', methods=['GET','POST'])
def home():
	return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', var=name, var2=True)
	else:
		return render_template('friend_exists.html', var=name, var2=False)






if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True,
    port = 8001
	)
