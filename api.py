from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'degf'

@app.route('/')
def home():
	return render_template('home.html', title ='home' )

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/contact')
def contact():
	return render_template('contact.html', title='contact')

@app.route('/login',methods = ['POST','GET'])
def login():
	
	if request.method == 'POST':
		users = {'user1': 'abc', 'user2': 'def', 'user3': 'ghi', 'user4':'jkl','user5':'mno'}
		username = request.form['username']
		password = request.form['password']
		if username not in users:
			return "USer doesn't exist. Enter a valid one."
		if users[username] != password:
			return "Invalid Password. Retry."
		
		session['username'] = username
		return redirect(url_for('home')) 


	#return render_template('home.html')
	return redirect(url_for('home'))

@app.route('/logout')
def logout():

	session.clear()
	return redirect(url_for('home'))

app.run(debug = True)
