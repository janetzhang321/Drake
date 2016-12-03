from flask import Flask, render_template, request, url_for, session, redirect

app= Flask(__name__)

@app.route("/")
@app.route("/home/", methods = ['POST'])
def home():
    return render_template('index.html')

@app.route('/result/')
def result():
	return render_template('result.html')

if __name__ == "__main__": 
	app.debug = True
	app.run()