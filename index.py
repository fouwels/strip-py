from flask import Flask, request, make_response, send_file

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def img():
	if request.method == 'GET':
		return "yo, you forgot to post"
	else:
		img = request.files['image'].read()
		
		return img;
	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')