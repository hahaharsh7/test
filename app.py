from flask import Flask , render_template , request
app = Flask(__name__)
@app.route('/send' , methods=['GET' , 'POST'])
def send():
	if request.method == 'POST':
		tell = request.form['tell']

		return render_template('tell.html' , tell=tell)

	return render_template('index.html')

if __name__=="__main__":
	app.run()
