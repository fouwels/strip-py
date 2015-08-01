from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def img():
	if request.method == 'GET':
		return "yo, you forgot to post"
	
	img = request.form['image']
	return img

	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')