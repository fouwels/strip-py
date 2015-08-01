import StringIO

from flask import Flask, request, make_response, send_file
from PIL import Image #not actually Pil, pillow

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def img():
	if request.method == 'GET':
		return "yo, you forgot to post"
	else:
		img = Image.open(request.files['image'])
		
		pixels = img.load()
		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
		        if pixels[x, y] == (255, 255, 255, 255):
		            pixels[x, y] = (255, 255, 255, 0)
		
		
		output = StringIO.StringIO()
		img.save(output, format="PNG")
		contents = output.getvalue()
		output.close()
		
		responseData = contents
		
		resp = make_response(responseData)
		resp.statusCode = 200
		return resp
	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')