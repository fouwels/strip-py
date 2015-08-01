from flask import Flask, request, make_response, send_file
from PIL import Image #not actually Pil, pillow

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def img():
	if request.method == 'GET':
		return "yo, you forgot to post"
	else:
		img = Image.open(request.files['image'])
		
		responseData = str(img.size);
		
		resp = make_response(responseData)
		resp.statusCode = 200
		return resp
	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')